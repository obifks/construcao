import json


class Lounge:

    empreendimento = []
    
    def __init__(self, unidade, vaga, price, real_price):
        self.unit = unidade
        self.vaga = vaga
        self.price = price
        self.real_price = real_price
        Lounge.empreendimento.append(self)
    
    @classmethod
    def save_data(cls):
        data = []
        for instance in Lounge.empreendimento:
            data.append({
                'unit': instance.unit,
                'vaga': instance.vaga,
                'price': instance.price,
                'real_price': instance.real_price,
            })
        with open('empreendimento_data.json', 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_data(cls):
        try:
            with open('empreendimento_data.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    Lounge(item['unit'], item['vaga'], item['price'], item['real_price'])
        except (FileNotFoundError, json.JSONDecodeError):
            print('Arquivo não encontrado ou inválido, iniciando atualização.')

    @classmethod
    def del_data(cls):
        unit_to_delete = input('Insira a unidade para deletar: ')
        Lounge.empreendimento = [instance for instance in Lounge.empreendimento if instance.unit != unit_to_delete]
        print(f'Unidade {unit_to_delete}, deletada com sucesso.')
        Lounge.save_data()

def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Insira um número.")


# Carregar os dados existentes
Lounge.load_data()

# Deletar unidade, se necessário
delete_choice = input('Deseja deletar uma unidade? S/N: ').lower()
if delete_choice == 's':
    Lounge.del_data()

# Adicionar nova unidade
finsert = input('Insira o número da unidade: ')
f_vaga = input('Insira o número da vaga: ')
fprice = input_number('Insira o preço total da unidade: ')
f_price_real = input_number('Insira o preço de venda da unidade: ')

lounge_instance = Lounge(finsert, f_vaga, fprice, f_price_real)

perdido = fprice - f_price_real
# Mostrar todas as unidades
print("\n--- Empreendimentos Cadastrados ---")
for instance in Lounge.empreendimento:
    print(f"Unidade: {instance.unit}")
    print(f"Vaga escolhida: {instance.vaga}")
    print(f"Preço Total: R${float(instance.price):,.2f}")
    print(f"Preço Pago: R${float(instance.real_price):,.2f}")
    print(f"Deixou de receber: R${float(perdido):,.2f}")
    print('-' * 40)

# Salvar dados
Lounge.save_data()
