import math as mt
import datetime
from prettytable import PrettyTable

user_data = {
        "John" : "SS102",
        "Agnes": "SS099",
        "Syifa": "SS100",
        "Ahsan": "SS101",
        "Ali"  : "SS098",
    }

product = {
        1:{"nama":"Brownies Coklat", "jenis": "Cake","qty":17, "expdate": "1/10/2025","harga":40000},
        2:{"nama":"Brownies Pandan", "jenis": "Cake","qty":15, "expdate": "1/10/2025","harga":40500},
        3:{"nama":"Dessert Box Nutela", "jenis": "Cake","qty":10, "expdate": "1/10/2025","harga":38000},
        4:{"nama":"Dessert Box Cadbury", "jenis": "Cake","qty":14, "expdate": "1/10/2025","harga":35000},
        5:{"nama":"Cookies", "jenis": "Cake","qty":12, "expdate": "5/10/2025","harga":22000},
        6:{"nama":"Croissant", "jenis": "Pastry","qty":9, "expdate": "1/10/2025","harga":14500},
        7:{"nama":"Pain au Chocolat", "jenis": "Pastry","qty":12, "expdate": "15/10/2025","harga":15000},
        8:{"nama":"Puff Pastry", "jenis": "Pastry","qty":14, "expdate": "15/10/2025","harga":18000},
        9:{"nama":"Garlic Bread", "jenis": "Bread","qty":8, "expdate": "1/10/2025","harga":19000},
        10:{"nama":"Cupcakes", "jenis": "Bread","qty":15, "expdate": "15/10/2025","harga":10000},
        11:{"nama":"Floss Bread", "jenis": "Bread","qty":15, "expdate": "15/10/2025","harga":8500},
        12:{"nama":"Thai Tea", "jenis": "Beverage","qty":20, "expdate": "15/10/2025","harga":15000},
        13:{"nama":"Iced Coffee Latte", "jenis": "Beverage","qty":19, "expdate": "15/10/2025","harga":21000},
        14:{"nama":"Iced Tea", "jenis": "Beverage","qty":21, "expdate": "15/10/2025","harga":15000},
        15:{"nama":"Iced Americano", "jenis": "Beverage","qty":8, "expdate": "15/10/2025","harga":17000},
}

cart = []

def menu_title(title):
    length = len(title)
    border = "-" * length
    print("\n" + border)
    print(title)
    print(border)

def show_all_product():
    table = PrettyTable()
    table.field_names = ["No", "Nama Produk", "Jenis Produk", "Qty", "Harga"]

    for product_number in sorted(product.keys()):
        item = product[product_number]
        table.add_row([product_number, item["nama"], item["jenis"], item["qty"], item["harga"]])

    print(table)

def product_list():
    while True:
        menu_title("Stock Items")
        print("1. Show All Product")
        print("2. Show by Product Types")
        print("3. Search Using Keywords")
        print("4. Back to Main Menu")
        choose_visual = input("Select Stock Display (1-4): ")
        if choose_visual == "1":
            show_all_product()
            
        elif choose_visual == "2":
            menu_title("Product Types")
            print("1. Cake")
            print("2. Pastry")
            print("3. Bread")
            print("4. Beverage")
            print("5. Back to Menu")
            choose_category = input("Select Product Category (1-4): ")
            if choose_category == "1":
                x = PrettyTable()
                x.field_names = ["No.", "Nama Barang", "Jenis Produk", "Qty", "Expired date", "Harga"]
                for key, value in product.items():
                    if value["jenis"] == "Cake":
                        x.add_row([key, value["nama"], value["jenis"], value["qty"], value["expdate"], value["harga"]])
                print(x)
            elif choose_category == "2":
                x = PrettyTable()
                x.field_names = ["No.", "Nama Barang", "Jenis Produk", "Qty", "Expired date", "Harga"]
                for key, value in product.items():
                    if value["jenis"] == "Pastry":
                        x.add_row([key, value["nama"], value["jenis"], value["qty"], value["expdate"], value["harga"]])
                print(x)
            elif choose_category == "3":
                x = PrettyTable()
                x.field_names = ["No.", "Nama Barang", "Jenis Produk", "Qty", "Expired date", "Harga"]
                for key, value in product.items():
                    if value["jenis"] == "Bread":
                        x.add_row([key, value["nama"], value["jenis"], value["qty"], value["expdate"], value["harga"]])
                print(x)
            elif choose_category == "4":
                x = PrettyTable()
                x.field_names = ["No.", "Nama Barang", "Jenis Produk", "Qty", "Expired date", "Harga"]
                for key, value in product.items():
                    if value["jenis"] == "Beverage":
                        x.add_row([key, value["nama"], value["jenis"], value["qty"], value["expdate"], value["harga"]])
                print(x)
            elif choose_category == "5":
                continue
            else:
                print("Input salah, silakan coba lagi.")
        elif choose_visual == "3":
            item_cari = input("Masukkan kata kunci barang yang ingin ditampilkan: ")
            search_results = []
            for key, value in product.items():
                if item_cari.lower() in value["nama"].lower():
                    value["key"] = key
                    search_results.append(value)
            if not search_results:
                print("Tidak ada hasil yang ditemukan.")
            else:
                x = PrettyTable()
                x.field_names = ["No.", "Nama Barang", "Jenis Produk", "Qty", "Expired date", "Harga"]
                for i, result in enumerate(search_results, start=1):
                    x.add_row([result["key"], result["nama"], result["jenis"], result["qty"], result["expdate"], result["harga"]])
                print(x)
        elif choose_visual == "4":
            break 
        else:
            print("Input salah, silakan coba lagi.")
            
#Date time
def is_valid_date(date_str): 
    try:
        datetime.datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
#Add stock
def add_stock():
    while True:
        new_id = len(product) + 1
        input_nama = input("Masukkan Nama Produk yang Ingin Ditambahkan: ").capitalize()
        item_baru = input_nama.replace(" ","")
        while len(item_baru) > 25:
            print("Max character = 25, try again🐝")
            input_nama = input("Masukkan Nama Produk yang Ingin Ditambahkan: ").capitalize()
            item_baru = input_nama.replace(" ","")
        if item_baru.lower() not in [product[key]['nama'].replace(" ","").lower() for key in product.keys()]:
            input_jenis = input("Masukkan Jenis dari Produk Baru: ").capitalize()
            while len(input_jenis) > 25:
                print("Max character = 25, try again🐝")
                input_jenis = input("Masukkan Jenis dari Produk Baru: ").capitalize()
            while True:
                try:
                    input_qty = int(input("Masukkan Jumlah Stok dari Produk Baru: "))
                    if input_qty <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. The minimum allowed quantity is 1. Try again!).")
            while True:
                input_exp_date = str(input("Masukkan expired date: "))
                if not is_valid_date(input_exp_date):
                    print("\nInvalid input. Date must be in the 'dd/mm/yyyy' format.\n")
                    continue
                break
            while True:
                try:
                    input_harga = int(input("Masukkan Harga per Unit dari Produk Baru: "))
                    if input_harga <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Price must be greater than 0. Try again!")
            checker2 = input(f"Apakah anda yakin ingin menambahkan produk {input_nama}, jenis {input_jenis}, dengan jumlah {mt.ceil(input_qty)}, expired date {input_exp_date}, dan harga {input_harga}? (Y/N): ")
            if checker2.lower() != "y":
                break
            else:
                product[new_id] = {
                "nama": input_nama.title(),
                "jenis": input_jenis.title(),
                "qty": mt.ceil(input_qty),
                "expdate": input_exp_date,
                "harga": input_harga
                }
                show_all_product()
                x = PrettyTable()
                x.field_names = ["No.", "Nama Barang", "Jenis Produk", "Qty", "Expired date", "Harga"]
                x.add_row([new_id, input_nama.title(), input_jenis.title(), mt.ceil(input_qty), input_exp_date, input_harga])
                print("Berikut detail barang yang ditambahkan:")
                print(x)
                break
        else:
            print("Invalid input. Item already exists.")
            break

#Update Stock 
def update_stock():
    while True:
        # Show all products
        show_all_product()

        # Input product number to update
        try:
            product_number = int(input("\nMasukkan nomor produk yang ingin diupdate: "))
        except ValueError:
            print("Invalid input. Please enter a number!")
            continue

        # Special code for admin to back to the main menu
        if product_number == -1:
            print("You chose to back to the main menu.")
            break

        if product_number not in product:
            print("Nomor produk tidak ditemukan, silahkan coba lagi.")
            continue

        while True:
            # Update field
            print("\nSelect the field you want to update: ")
            print("1. Nama Barang")
            print("2. Jenis Produk")
            print("3. Qty")
            print("4. Expired Date")
            print("5. Harga")
            print("\nOr:\n6. Back")

            field_choice = input("\nEnter your choice (1-6): ")

            try:
                field_choice = int(field_choice)
                if field_choice in [1, 2, 3, 4, 5, 6]:
                    break
                else:
                    print("\nInvalid choice. Please try again!", end="")
            except ValueError:
                print("\nInvalid input. Please enter a number!", end="")

        if field_choice == 6:
            continue

        # Handle update for each field
        update_mapping = {
            1: {"field": "nama", "prompt": "Masukkan nama baru: "},
            2: {"field": "jenis", "prompt": "Masukkan jenis baru: "},
            3: {"field": "qty", "prompt": "Masukkan jumlah stok baru: ", "validation": lambda x: x.isdigit()},
            4: {"field": "expdate", "prompt": "Masukkan tanggal kadaluarsa baru (dd/mm/yyyy): "},
            5: {"field": "harga", "prompt": "Masukkan harga baru: ", "validation": lambda x: x.isdigit()},
        }

        update_info = update_mapping[field_choice]
        field_name = update_info["field"]
        new_value = input(update_info["prompt"])

        if "validation" in update_info:
            while not update_info["validation"](new_value):
                new_value = input(f"Input not valid. {update_info['prompt']}")

        confirmation = input(f"Apakah Anda yakin ingin mengubah {field_name} '{product[product_number][field_name]}' menjadi '{new_value}'? (Y/N): ")
        if confirmation.lower() == 'y':
            product[product_number][field_name] = int(new_value) if field_choice in [3, 5] else new_value

            # Print updated product list
            print(f"\nProduk nomor {product_number} telah berhasil diubah! Berikut adalah list produk terbaru Anda.")
            show_all_product()

            # Ask user if they want to update another product or return to the main menu
            update_another = input("Apakah Anda masih ingin melakukan update pada produk yang lain? (Y/N): ")
            while update_another not in ['y', 'n']:
                update_another = input("Masukkan 'y' atau 'n': ")
            if update_another == 'n':
                break

#Delete Stock
def delete_stock():
    show_all_product()
    while True:
        try:
            item_id = int(input("Masukkan nomor produk yang ingin dihapus: "))
        except ValueError:
            print("Invalid input. Please enter a number!")
            continue
        
        if item_id not in product:
            print(f"Produk dengan nomor {item_id} tidak ditemukan!\n")
            continue
        else:
            nama_produk = product[item_id]['nama']
            checker = input(f"Apakah Anda yakin ingin menghapus '{nama_produk}' dari daftar produk? (Y/N): ")
            if checker.lower() != "y":
                print("\nThe deletion process has been cancelled.")
                break
            else:
                del product[item_id]
                print(f"\n'{nama_produk}' telah berhasil dihapus!")
                show_all_product()
                break

# Buy Product
def buy_product():
    show_all_product()
    while True:
        input_beli = input("Masukkan No. Produk Yang Ingin Dibeli: ")
        try:
            product_number = int(input_beli)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if product_number not in product:
            print(f"Produk dengan nomor \"{input_beli}\" tidak ditemukan")
        else:
            qty_beli = int(input("Masukkan Jumlah Yang Ingin Dibeli: "))
            if qty_beli <= 0:
                print("Jumlah pembelian tidak boleh kurang dari 1")
            elif qty_beli > product[product_number]["qty"]:
                print(f"Stok tidak cukup. Stok {product[product_number]['nama']} sisa {product[product_number]['qty']}")
            else:
                product[product_number]["qty"] -= qty_beli
                cart.append({"nama_produk": product[product_number]["nama"],
                             "jenis_produk": product[product_number]["jenis"],
                             "qty": qty_beli,
                             "harga": product[product_number]["harga"]})
                print(f"Berhasil membeli {qty_beli} \"{product[product_number]['nama']}\".")
                checker = input("Apakah Ingin Membeli Item Lain? (Y/N): ")
                if checker.upper() != "Y":
                    break

    if len(cart) > 0:
        print("Keranjang Belanja")
        table = PrettyTable()
        table.field_names = ["Nama Produk", "Jenis Produk", "Qty", "Harga", "Total Harga"]
        total = 0
        for item in cart:
            table.add_row([item["nama_produk"], item["jenis_produk"], item["qty"], item["harga"], item["qty"] * item["harga"]])
            total += item["qty"] * item["harga"]
        print(table)
        
        while True:
            print('Total Yang Harus Dibayar = {}'.format(total))
            cash = int(input('Masukkan jumlah uang : '))
            if cash > total:
                kembali = cash - total
                print('Thank you for shopping in Sweet Savory. Toodles🍰👋 \n\nChange money : {}'.format(kembali))
                cart.clear()
                break
            elif cash == total:
                print('Thank you for shopping in Sweet Savory. Toodles🍰👋')
                cart.clear()
                break
            else:
                uang_kurang = total - cash
                print('Your money is not enough, you are short of Rp {}'.format(uang_kurang))
                decision = input('Do you want to add more money or cancel the purchase? (Add/Cancel): ')
                if decision.lower() == 'cancel':
                    print('Purchase canceled. Please come back again.')
                    cart.clear()
                    break
                elif decision.lower() == 'add':
                    continue
                else:
                    print('Invalid option, please try again.')

# Log in interface    
last_username = None

def print_header(title):
    length = len(title)
    border = "-" * (length + 6)
    print(f" {' '}{border}{' '}")
    print(f"|  {title}  |")
    print(f" {' '}{border}{' '}")

while True:
    print_header("🍞🍪 Sweet Savory Bakery 🍰🥐")
    print("\nPlease select an option:")
    print("1. Employee Login")
    print("2. Customer Login")
    print("3. Close the Program")

    # Keep asking for choice until a valid input is entered
    while True:
        try:
            choice = input("\nEnter your choice (1-3): ")
            if choice.isspace() or not choice:
                print("\nYou didn't enter anything!", end="")
            elif choice.startswith("+"):
                print("\nInvalid choice. Please try again!", end="")
            elif int(choice) not in [1, 2, 3]:
                print("\nInvalid choice. Please try again!", end="")
            else:
                choice = int(choice)
                break
        except ValueError:
            print("\nInvalid input. Please enter a number!", end="")

    if choice == 1:
        # Employee login menu
        username = input("\nEnter your username: ").capitalize()
        password = input("Enter your password: ").upper()
        if username in user_data and user_data[username] == password:
            menu_title("Employee Main Menu")
            if last_username == username:
                print(f"\nWelcome back, {username}!")
            else:
                print(f"\nWelcome, {username}!")
            while True:
                print("\nPlease select an option:")
                print("1. Show Stock Items")
                print("2. Add Items")
                print("3. Update Stock Items")
                print("4. Delete Stock Items")
                print("5. Log Out")

                # Keep asking for employee_choice until a valid input is entered
                while True:
                    try:
                        employee_choice = input("\nEnter your choice (1-5): ")
                        if employee_choice.isspace() or not employee_choice:
                            print("\nYou didn't enter anything!", end="")
                        elif employee_choice.startswith("+"):
                            print("\nInvalid choice. Please try again!", end="")
                        elif int(employee_choice) not in [1, 2, 3, 4, 5]:
                            print("\nInvalid choice. Please try again!", end="")
                        else:
                            employee_choice = int(employee_choice)
                            break
                    except ValueError:
                        print("\nInvalid input. Please enter a number!", end="")

                if employee_choice == 1:
                    product_list()
                elif employee_choice == 2:
                    add_stock()
                elif employee_choice == 3:
                    update_stock()
                elif employee_choice == 4:
                    delete_stock()
                elif employee_choice == 5:
                    print(f"\nLogged out successfully! See you next time, {username}!\n")
                    last_username = username
                    break
        else:
            print("\nInvalid username or password!\n")

    elif choice == 2:
        Name = input("Enter your name: ").capitalize()
        menu_title(f"Welcome to Sweet Savory🍰🥐, {Name}!")
        while True:
            print("\nPlease select an option:")
            print("1. Show Stock Items")
            print("2. Buy Items")
            print("3. Log Out")

            #Keep asking the customer until the valid option selected
            while True:
                try:
                    customer_choice = input("Enter your choice (1-3): ")
                    if customer_choice.isspace() or not customer_choice:
                        print("Please input something!", end="")
                    elif customer_choice.startswith("+"):
                        print("Invalid input", end="")
                    elif int(customer_choice) not in [1, 2, 3]:
                        print("Invalid input", end="")
                    else:
                        customer_choice = int(customer_choice)
                        break
                except ValueError:
                    print("Invalid input.\nEnter a valid number!", end="")

            if customer_choice == 1:    
                product_list()   
            elif customer_choice == 2:
                buy_product()
            elif customer_choice == 3:
                print(f"Logged out successful. See you next time! Toodles🍰👋, {Name}.")
                break
            else:
                print("Invalid input!")

    elif choice == 3:
        print("\nSee you around!\n")
        break
