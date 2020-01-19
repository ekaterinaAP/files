print("Книга рецептов")
with open("recipes.txt") as recipe:
    print(recipe.read())

    #задача 1
    recipe.seek(0)

    def output_cook_book(recipes):  
        cook_book = {}
    
        while True:
            dish = recipes.readline().strip()        
            if not dish:
                break

            number = int(recipes.readline().strip())        
        
            ingredients = []
            cook_book[dish] = ingredients

            count = 0
            while count < number:
                ingredient = recipes.readline().strip()
                ingredient_list = ingredient.split("|")            
                ingredients.append({"ingredient_name": ingredient_list[0], "quantity": ingredient_list[1], "measure": ingredient_list[2]})
                count +=1

            #пустая строка
            recipes.readline().strip()     
        
        return cook_book

    print() 
    cook_book = output_cook_book(recipe)      
    for dish in cook_book:
        print(dish)
        for ingredient in cook_book[dish]:
            print(ingredient)
    

    #задача 2
    recipe.seek(0)

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}

        while True:
            dish = recipe.readline().strip()        
            if not dish:
                break

            number = int(recipe.readline().strip())            

            count = 0
            while count < number:
                ingredient = recipe.readline().strip()
                ingredient_list = ingredient.split("|")            
                if dish in dishes:
                    shop_list[ingredient_list[0]] = {"measure": ingredient_list[2], "quantity": int(ingredient_list[1])*person_count}

                count +=1

            recipe.readline().strip()

        return shop_list

    try:
        food = input("Перечислите блюда через запятую, которые нужно приготовить: ")
        person = int(input("Укажите количество порций: "))
        print("Состав блюд:")
    except Exception as e:
        print(e)
        print("Вы ошиблись при вводе")
        print("Состав блюд для Омлета,Утки по-пекински,Запеченного картофеля,Фахитос на одну порцию")
        food = "Омлет,Утка по-пекински,Запеченый картофель,Фахитос"
        person = 1
    
    dishes_list = food.split(",")      
    
    shop_list = get_shop_list_by_dishes(dishes_list, person)
    for ingredient in shop_list:
        print(ingredient, shop_list[ingredient])
      

        