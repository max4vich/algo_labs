def gardener_count(m, n):  # m - рядки, а n - стовпці
    result_array = []
    for i in range(m):
        for j in range(n):
            if i % 2 == 0:
                result_array.append(i * n + j + 1)
            else:
                result_array.append(i * n + n - j)
    return result_array


if __name__ == "__main__":
    print(gardener_count(4, 3))
