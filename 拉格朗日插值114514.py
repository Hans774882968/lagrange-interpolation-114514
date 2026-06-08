import sympy as sp


def main():
    x = sp.Symbol('x')
    while True:
        try:
            line1 = input("\n请输入点的个数 n (正整数) 或 'q' 退出: ").strip()
            if not line1:
                continue
            if line1.lower() == 'q' or line1.lower() == 'quit':
                break

            n = int(line1)
            if n <= 0:
                print("错误: n 必须是一个正整数QwQ")
                continue

            line2 = input(f"请输入 {n} 个整数 (用空格分隔，表示 a[1] 到 a[{n}]): ").strip()
            a_list = line2.split()

            if len(a_list) != n:
                print(f"错误: 需要 {n} 个整数，但收到了 {len(a_list)} 个。请重新输入QwQ")
                continue

            a = [sp.S(val) for val in a_list]

            points = [(i, a[i - 1]) for i in range(1, n + 1)]

            P = sp.S(0)

            for i in range(n):
                xi, yi = points[i]

                Li = sp.S(1)
                for j in range(n):
                    if i != j:
                        xj, _ = points[j]
                        Li *= (x - xj) / (xi - xj)

                P += yi * Li

            P_expanded = sp.expand(P)

            print("-" * 50)
            print(f"展开后的插值多项式为:\n{P_expanded}")
            print(sp.latex(P_expanded))
            print("-" * 50)

        except ValueError:
            print("输入格式错误，请确保第一行为正整数或'q'，第二行为空格分隔的整数QwQ")
        except EOFError:
            print("\n检测到输入结束，程序退出QwQ")
            break
        except Exception as e:
            print(f"发生未知错误: {e}")


if __name__ == "__main__":
    main()
