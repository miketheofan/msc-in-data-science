import snap
import time
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)


def generate_watts_strogatz(num_nodes, out_degree=10, rewire_prob=0.1):
    return snap.GenSmallWorld(num_nodes, out_degree, rewire_prob)


def find_max_degree_node(graph):
    max_deg = -1
    max_node = -1

    for node in graph.Nodes():
        deg = node.GetDeg()
        if deg > max_deg:
            max_deg = deg
            max_node = node.GetId()

    return max_node, max_deg


def find_top_hits_nodes(graph):
    HubH = snap.TIntFltH()
    AuthH = snap.TIntFltH()
    snap.GetHits(graph, HubH, AuthH)

    max_hub_score = max(HubH[node] for node in HubH)
    max_hub_node = [node for node in HubH if HubH[node] == max_hub_score][0]

    max_auth_score = max(AuthH[node] for node in AuthH)
    max_auth_node = [node for node in AuthH if AuthH[node] == max_auth_score][0]

    return max_hub_node, max_hub_score, max_auth_node, max_auth_score


def time_community_detection(graph, timeout=600):
    CmtyV = snap.TCnComV()

    # Girvan-Newman
    start = time.time()
    try:
        snap.CommunityGirvanNewman(graph, CmtyV)
        gn_time = time.time() - start
        if gn_time > timeout:
            gn_status = f"TIMEOUT ({gn_time:.2f}s > {timeout}s)"
        else:
            gn_status = f"{gn_time:.2f}s"
    except Exception as e:
        gn_status = f"FAILED"

    # Clauset-Newman-Moore
    start = time.time()
    try:
        snap.CommunityCNM(graph, CmtyV)
        cnm_time = time.time() - start
        if cnm_time > timeout:
            cnm_status = f"TIMEOUT ({cnm_time:.2f}s)"
        else:
            cnm_status = f"{cnm_time:.2f}s"
    except Exception as e:
        cnm_status = f"FAILED"

    return gn_status, cnm_status


def analyze_top_pagerank_nodes(graph, top_n=30):
    print(f"  Calculating centrality measures...")

    # 1. Calculate PageRank
    print("    - PageRank...")
    PRankH = snap.TIntFltH()
    snap.GetPageRank(graph, PRankH)

    # 2. Calculate Betweenness for all nodes
    print("    - Betweenness (this may take time)...")
    BtwH = snap.TIntFltH()
    EdgeBtwH = snap.TIntPrFltH()
    snap.GetBetweennessCentr(graph, BtwH, EdgeBtwH, 1.0)

    # 3. Calculate HITS scores
    print("    - HITS (Hub & Authority)...")
    HubH = snap.TIntFltH()
    AuthH = snap.TIntFltH()
    snap.GetHits(graph, HubH, AuthH)

    # 4. Build DataFrame with all measures
    print("    - Closeness (per-node)...")
    data = []
    node_count = 0
    total_nodes = graph.GetNodes()

    for node in PRankH:
        if node_count % 100 == 0:
            print(f"      Processed {node_count}/{total_nodes} nodes...")

        data.append({
            'node_id': node,
            'pagerank': PRankH[node],
            'betweenness': BtwH[node] if node in BtwH else 0,
            'closeness': snap.GetClosenessCentr(graph, node),
            'authority': AuthH[node] if node in AuthH else 0,
            'hub': HubH[node] if node in HubH else 0
        })
        node_count += 1

    df = pd.DataFrame(data)

    # 5. Sort by PageRank and get top-N
    df_sorted = df.sort_values('pagerank', ascending=False).head(top_n)

    return df_sorted


def normalize(values):
    values = np.array(values)
    min_val, max_val = values.min(), values.max()
    if max_val == min_val:
        return np.zeros_like(values)
    return (values - min_val) / (max_val - min_val)


def create_plots(df_top30, output_dir="."):
    print("\n  Creating visualization plots...")

    # Plot 1: Betweenness, Closeness, PageRank
    print("    - Plot 1: Betweenness, Closeness, PageRank...")
    fig, ax = plt.subplots(figsize=(14, 7))
    x = np.arange(30)

    ax.plot(x, normalize(df_top30['betweenness'].values),
            marker='o', label='Betweenness', linewidth=2, markersize=6)
    ax.plot(x, normalize(df_top30['closeness'].values),
            marker='s', label='Closeness', linewidth=2, markersize=6)
    ax.plot(x, normalize(df_top30['pagerank'].values),
            marker='^', label='PageRank', linewidth=2, markersize=6)

    ax.set_xlabel('Top-30 Nodes (ranked by decreasing PageRank)', fontsize=12)
    ax.set_ylabel('Normalized Centrality Score', fontsize=12)
    ax.set_title('Centrality Measures Comparison', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plot1_path = f"{output_dir}/plot1_centrality.png"
    plt.savefig(plot1_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"      Saved: {plot1_path}")

    # Plot 2: PageRank, Authority, Hub
    print("    - Plot 2: PageRank, Authority, Hub...")
    fig, ax = plt.subplots(figsize=(14, 7))
    x = np.arange(30)

    ax.plot(x, normalize(df_top30['pagerank'].values),
            marker='o', label='PageRank', linewidth=2, markersize=6)
    ax.plot(x, normalize(df_top30['authority'].values),
            marker='s', label='Authority', linewidth=2, markersize=6)
    ax.plot(x, normalize(df_top30['hub'].values),
            marker='^', label='Hub', linewidth=2, markersize=6)

    ax.set_xlabel('Top-30 Nodes (ranked by decreasing PageRank)', fontsize=12)
    ax.set_ylabel('Normalized Score', fontsize=12)
    ax.set_title('PageRank vs HITS Scores', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plot2_path = f"{output_dir}/plot2_hits.png"
    plt.savefig(plot2_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"      Saved: {plot2_path}")


def main():
    # Parameters
    sizes = [50, 500]
    out_degree = 10
    rewire_prob = 0.1

    print("=" * 70)
    print("PROJECT 2 - PART 2: COMMUNITY DETECTION ANALYSIS")
    print("=" * 70)
    print(f"\nParameters:")
    print(f"  Graph sizes: {sizes}")
    print(f"  Out-degree: {out_degree}")
    print(f"  Rewiring probability: {rewire_prob}")
    print("=" * 70)

    results = []
    graphs = {}

    for i, size in enumerate(sizes, 1):
        print(f"\n{'='*70}")
        print(f"[{i}/{len(sizes)}] Analyzing graph with {size} nodes...")
        print(f"{'='*70}")

        # Generate graph
        print(f"  Generating Watts-Strogatz graph...")
        graph = generate_watts_strogatz(size, out_degree, rewire_prob)
        graphs[size] = graph
        print(f"    ✓ Nodes: {graph.GetNodes()}, Edges: {graph.GetEdges()}")

        # Find max degree node
        print(f"  Finding max degree node...")
        max_node, max_deg = find_max_degree_node(graph)
        print(f"    ✓ Max Degree: Node {max_node} (degree: {max_deg})")

        # Find top HITS scores
        print(f"  Calculating HITS scores...")
        hub_node, hub_score, auth_node, auth_score = find_top_hits_nodes(graph)
        print(f"    ✓ Top Hub: Node {hub_node} (score: {hub_score:.6f})")
        print(f"    ✓ Top Authority: Node {auth_node} (score: {auth_score:.6f})")

        # Time community detection
        print(f"  Running community detection algorithms...")
        gn_time, cnm_time = time_community_detection(graph)
        print(f"    ✓ Girvan-Newman: {gn_time}")
        print(f"    ✓ Clauset-Newman-Moore: {cnm_time}")

        # Store results
        results.append({
            'size': size,
            'nodes': graph.GetNodes(),
            'edges': graph.GetEdges(),
            'max_node': max_node,
            'max_deg': max_deg,
            'hub_node': hub_node,
            'hub_score': hub_score,
            'auth_node': auth_node,
            'auth_score': auth_score,
            'gn_time': gn_time,
            'cnm_time': cnm_time
        })

    # Display results table
    print(f"\n{'='*70}")
    print("RESULTS SUMMARY")
    print(f"{'='*70}")
    df_results = pd.DataFrame(results)
    print(df_results.to_string(index=False))

    # Analyze largest graph with PageRank
    largest_size = max(sizes)
    print(f"\n{'='*70}")
    print(f"PageRank Analysis for {largest_size} nodes graph")
    print(f"{'='*70}")

    df_top30 = analyze_top_pagerank_nodes(graphs[largest_size])

    print(f"\nTop-30 Nodes by PageRank:")
    print(df_top30.to_string(index=False))

    # Create plots
    create_plots(df_top30)

    print(f"\n{'='*70}")
    print(" ANALYSIS COMPLETE!")
    print(f"{'='*70}")
    print("\nGenerated files:")
    print("  - plot1_centrality.png")
    print("  - plot2_hits.png")
    print("\nNext steps:")
    print("  1. Review the plots")
    print("  2. Answer the algorithm suitability questions in project2.pdf")
    print("  3. Include both plots in your report")


if __name__ == '__main__':
    main()
