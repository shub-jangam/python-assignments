import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

def label_cluster(row):
    """Label clusters based on centroid characteristics."""
    if row['G3'] >= 15 and row['failures'] <= 0.5 and row['studytime'] >= 2.5 and row['absences'] <= 5:
        return 'Top Performer'
    elif row['G3'] >= 10:
        return 'Average Student'
    else:
        return 'Struggling Student'

def cluster_summary(filePath):
    # Load dataset
    df = pd.read_csv(filePath, sep=';')
    print("Dataset Dimension:", df.shape)
    print(50 * "-")
    print(df.head())
    print(50 * "-")

    print("Statistical Summary")
    print(df.describe())
    print(50 * "-")

    # Selected features
    features = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']
    X = df[features]

    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)

    # Get cluster centers (in original scale)
    centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=features)
    print("Cluster Centers (Original Scale):\n", centroids)
    print(50 * "-")

    # Label clusters based on centroid characteristics
    centroids['performance_category'] = centroids.apply(label_cluster, axis=1)

    # Map cluster numbers to performance labels
    cluster_map = dict(zip(centroids.index, centroids['performance_category']))
    df['performance_category'] = df['cluster'].map(cluster_map)

    # PCA for 2D Visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    df['pca1'] = X_pca[:, 0]
    df['pca2'] = X_pca[:, 1]

    # Plotting clusters
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='pca1', y='pca2', hue='performance_category', palette='Set1')
    plt.title("Student Clusters (via PCA)")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.legend(title="Cluster")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    cluster_summary("student-mat.csv")

if __name__ == "__main__":
    main()
