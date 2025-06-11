def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}
    try:
        with open(input_file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if parts:
                    ip = parts[0]
                    if ip in allowed_ips:
                        ip_counts[ip] = ip_counts.get(ip, 0) + 1
        with open(output_file_path, 'w') as out_file:
            for ip, count in ip_counts.items():
                out_file.write(f"{ip} - {count}\n")
        print(f" Результати збережено у файл: {output_file_path}")
    except FileNotFoundError:
        print(f" Вхідний файл не знайдено: {input_file_path}")
    except IOError as e:
        print(f" Помилка при записі у файл: {e}")

allowed_ips = ["83.149.9.216", "66.249.73.135"]
filter_ips("C:/Users/Maks PK/Downloads/apache_logs.txt", "C:/Users/Maks PK/Downloads/filtered_ips.txt", allowed_ips)
