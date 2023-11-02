import os.path

from product_management.Product import Product
from product_management.ProductOptions import ProductOptions


class ProductManagement:
    al = []
    file_path = r"C:\Users\ganuk\PycharmProjects\Shop_Management\product_management\Product.csv"

    @staticmethod
    def product_management():
        can_i_keep_running_the_program = True

        while can_i_keep_running_the_program:
            print("**** Welcome to Product Management *****")
            print("\n")
            print("What would you like to do?")
            print("1. Add Product")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. Search Product")
            print("5. Quit")

            option_selected_by_user = int(input())

            if option_selected_by_user == ProductOptions.QUIT:
                ProductManagement.save_data_to_file()
                print("!!! Program Closed !!!")
                can_i_keep_running_the_program = False

            elif option_selected_by_user == ProductOptions.ADD_PRODUCT:
                ProductManagement.add_product()
                print("\n")

            elif option_selected_by_user == ProductOptions.EDIT_PRODUCT:
                edit_product_name = input("Enter Product Name to edit :")
                ProductManagement.edit_user(edit_product_name)
                print("\n")

            elif option_selected_by_user == ProductOptions.SEARCH_PRODUCT:
                sp = input("Enter Product Name to search :")
                ProductManagement.search_user(sp)
                print("\n")

            elif option_selected_by_user == ProductOptions.DELETE_PRODUCT:
                delete_product = input("Enter Product Name to delete :")
                ProductManagement.delete_product(delete_product)
                print("\n")


    @staticmethod
    def add_product():
        p_object = Product()
        p_object.productName = input("Product Name :")
        p_object.productID = input("Product ID :")
        p_object.price = input("Price :")
        p_object.quantity = input("Quantity :")
        p_object.categoary = input("Categoary :")
        ProductManagement.al.append(p_object)

    @staticmethod
    def search_user(product_Name):
        for Product in ProductManagement.al:
            if Product.productName.lower() == product_Name.lower():
                ProductManagement.print_user_details(Product)
                return
        print("Product Not Found.")

    def delete_product(product_Name):
        for Product in ProductManagement.al:
            if Product.productName.lower() == product_Name.lower():
                ProductManagement.al.remove(Product)
                print(f"Product {Product.productName} has been deleted.")
                return
        print("Product Not Found.")

    @staticmethod
    def edit_user(product_name):
        for Product in ProductManagement.al:
            if Product.productName.lower() == product_name.lower():
                ProductManagement.print_user_details(Product)
                Product.productName = input("New Product Name:")
                Product.productID = input("New Product ID:")
                Product.price = input("New Product Price:")
                Product.quantity = input("New Product Quantity:")
                Product.categoary = input("New Product Categoary:")
                print("Product Information Updated.")
                return
        print("Product Not Found.")

    @staticmethod
    def print_user_details(Product):
        print("Product Name :" +Product.productName)
        print("Product ID: " + Product.productID)
        print("Price: " + Product.price)
        print("Quantity: " + Product.quantity)
        print("Category :"+Product.categoary)

    @staticmethod
    def load_data_from_file():
        if os.path.exists(ProductManagement.file_path):
            with open(ProductManagement.file_path, "r") as file:
                for line in file:
                    p_data = line.strip().split(",")
                    if len(p_data) > 4:
                        product = Product(p_data[0],p_data[1],p_data[2],p_data[3],p_data[4])
                        ProductManagement.al.append(Product)

    @staticmethod
    def save_data_to_file():
        print("Saving Product data to file")
        with open(ProductManagement.file_path,"a") as file:
            for Product in ProductManagement.al:
                file.write(f"{Product.productName},{Product.productID},{Product.price},{Product.quantity},{Product.categoary}\n")


