# 进阶版：输入DNA序列，统计碱基频率并计算GC含量

def analyze_dna(sequence):
    # 统一转为大写，防止大小写出错
    sequence = sequence.upper()
    
    # 过滤掉非ATCG的字符（比如空格、数字、X等）
    valid_bases = "ATCG"
    clean_seq = "".join([base for base in sequence if base in valid_bases])
    
    # 如果输入的全是不合法字符，提示错误
    if not clean_seq:
        return "错误：没有检测到有效的DNA序列(仅限ATCG)"

    # 统计每种碱基的数量
    counts = {base: clean_seq.count(base) for base in valid_bases}
    total_length = len(clean_seq)
    
    # 计算GC含量 (G和C的数量占总长度的比例 * 100)
    gc_content = (counts['G'] + counts['C']) / total_length * 100

    # 返回一个字典格式的结果
    return {
        "序列": clean_seq,
        "总长度": total_length,
        "A的数量": counts['A'],
        "T的数量": counts['T'],
        "C的数量": counts['C'],
        "G的数量": counts['G'],
        "GC含量(%)": round(gc_content, 2)
    }

# 接收用户输入
test_seq = input("请输入DNA序列(例如ATCG): ")
result = analyze_dna(test_seq)

# 格式化打印结果
print("\n--- 分析报告 ---")
if isinstance(result, dict):
    for key, value in result.items():
        print(f"{key}: {value}")
else:
    print(result)