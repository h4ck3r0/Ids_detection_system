def extract_features(pkt):
    try:
        if IP in pkt:
            proto = pkt.proto
            length = len(pkt)
            src_port = pkt.sport if hasattr(pkt, 'sport') else 0
            dst_port = pkt.dport if hasattr(pkt, 'dport') else 0
            return [proto, src_port, dst_port, length]
        return None
    except Exception as e:
        print(f"Feature extraction failed: {e}")
        return None