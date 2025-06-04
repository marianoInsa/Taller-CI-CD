# generador de datos de prueba "Texto" y "Cant" y guardar en un archivo CSV
import csv
import faker
def generate_data(num_rows):
    fake = faker.Faker()
    data = []
    for _ in range(num_rows):
        text = fake.text(max_nb_chars=20).rstrip('.')
        cant = fake.random_int(min=1, max=100)
        data.append([text, cant])
    return data

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Texto', 'Cant'])
        writer.writerows(data)

if __name__ == "__main__":
    num_rows = 100
    data = generate_data(num_rows)
    save_to_csv(data, 'data.csv')
    print(f"Datos generados y guardados en data.csv.")