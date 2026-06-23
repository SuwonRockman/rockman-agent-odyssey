from pyvis.network import Network

def create_network_html(records):
    """
    Neo4j에서 추출된 레코드 리스트를 받아 PyVis HTML 문자열로 변환합니다.
    """
    # Streamlit 다크 모드에 어울리는 배경색 및 글자색 적용
    net = Network(height='500px', width='100%', bgcolor='#0E1117', font_color='white', notebook=False)
    net.force_atlas_2based() # 물리 엔진 적용하여 예쁘게 퍼지게 함
    
    added_nodes = set()
    for r in records:
        src = r['source']
        tgt = r['target']
        rel = r['relationship']
        
        # 시작 노드 (빨간색)
        if src not in added_nodes:
            net.add_node(src, label=src, title=src, color='#FF4B4B', size=20)
            added_nodes.add(src)
            
        # 도착 노드 (녹색)
        if tgt not in added_nodes:
            net.add_node(tgt, label=tgt, title=tgt, color='#00CC96', size=15)
            added_nodes.add(tgt)
            
        # 엣지 추가
        net.add_edge(src, tgt, title=rel, label=rel, color='#888888')
        
    # generate_html()은 HTML 코드 문자열을 반환합니다.
    html_string = net.generate_html()
    return html_string
