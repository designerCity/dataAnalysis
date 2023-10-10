import pandas as pd
import networkx as nx
import geopandas as gpd
from shapely.geometry import LineString
import matplotlib.pyplot as plt
# adjacency_matrix = pd.read_csv('symmetric_matrix.csv', header = None)  # 파일 경로를 적절히 수정
adjacency_matrix = pd.read_csv('symmetric_matrix.csv' ,usecols=range(0, len(pd.read_csv('symmetric_matrix.csv').columns)))  # 파일 경로를 적절히 수정
adjacency_matrix = adjacency_matrix.iloc[:, 1:]

# 대칭 행렬로 변환 (가중치 데이터가 들어 있는 열 선택)
adjacency_matrix = adjacency_matrix.to_numpy()

# 빈 그래프 생성
G = nx.Graph()

# 대칭 행렬의 값을 기반으로 엣지 추가
num_nodes = adjacency_matrix.shape[1]
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        weight = adjacency_matrix[i, j]
        if weight > 0:
            G.add_edge(i, j, weight=weight)

# 노드의 위치 정보 (위경도) 포함하는 딕셔너리 생성
node_positions = {}
for i in range(num_nodes):
    latitude = lat_long['latitude'][i]  # 위도 컬럼 이름에 맞게 변경 필요
    longitude = lat_long['longitude'][i]  # 경도 컬럼 이름에 맞게 변경 필요
    
    node_positions[i] = (longitude, latitude)  # 경도와 위도 순서로 지정

# GeoDataFrame 생성 및 좌표 설정 (shape 파일 로드)
shapefile_path = '/Users/kimsh/Desktop/ExploratoryDataAnalysis/SGG_수도권_4326/SGG_수도권_4326.shp'
gdf_edges_original_crs = gpd.read_file(shapefile_path)

# Edge 의 방향 설정하는 방법
for u,v,w in G.edges(data=True):
    start_point_coords = node_positions[u]
    end_point_coords = node_positions[v]
    
    line_geom_forward = LineString([start_point_coords,end_point_coords])
    
    line_geom_backward=LineString([end_point_coords,start_point_coords])
    
    gdf_edges_original_crs.loc[len(gdf_edges_original_crs)]={'geometry':line_geom_forward}
    
    gdf_edges_original_crs.loc[len(gdf_edges_original_crs)]={'geometry':line_geom_backward}

target_crs_code = 'EPSG:4326'   # 목적지 좌표계 코드 (예: WGS84)

gdf_edges_transformed_crs = gdf_edges_original_crs.to_crs(target_crs_code)


plt.figure(figsize=(100, 100))

node_sizes_networkx= [10 for _ in range(num_nodes)]   # NetworkX 노드 크기 설정 (여기서는 일괄적으로 크기가 동일하게 설정되었습니다.)
edge_widths_networkx= [0.1 * G[u][v]['weight'] for u, v in G.edges()]   # NetworkX 엣지 너비 설정

nx.draw(G, pos=node_positions, node_color='yellow', width=edge_widths_networkx,
        node_size=node_sizes_networkx, alpha=0.01)

gdf_edges_transformed_crs.plot(ax=plt.gca(), color='red', linewidth=2, alpha=0.2)   # shape 파일 시각화
plt.savefig('output.png')   # 이미지 파일로 저장
# gdf_edges_transformed_crs.to_file('학령인구주거이동현황.shp')   # shape 파일로 저장
plt.show()
