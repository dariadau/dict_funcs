# dict_funcs (функции со словарями)
dict_funcs состоит из 3 функций: dict_converter, count_variatons и check_mismatch.  

#  1. **Что делает dict_converter?**        
   На входе есть список. В результате создается словарь, в котором каждый элемент списка является и ключом и значением.  

> [!NOTE]
> Пользователем задается $${\color{lightblue}один \space аргумент}$$ типа $${\color{lightblue}list}$$    
> $${\color{lightblue}Значение \space по \space умолчанию:}$$ _не задано_        

> [!TIP]  
> **Пример ввода-вывода:**       
> $${\color{lightgreen}input:}$$ _[1, 2, 3, 4]_       
> $${\color{lightgreen}output:}$$ _{1: 1, 2: 2, 3: 3, 4: 4}_
	
	
# 2. **Что делает count_variatons?**        
   Задается список, состоящий из положительных целых чисел. Функция возвращает количество кортежей типа  
   (a, b, c, d), которые можно создать из заданного списка.  
   В данных кортежах элементы не равны друг другу (a != b != c != d), а также действует следующее равенство:  
   произведение первых двух элементов равно произведению двух последних элементов (a * b = c * d).
   
> [!NOTE]
> Пользователем задается $${\color{lightblue}один \space аргумент}$$ типа $${\color{lightblue}list}$$    
> $${\color{lightblue}Значение \space по \space умолчанию:}$$ _не задано_

> [!TIP]      
> **Пример ввода-вывода:**        
> $${\color{lightgreen}input:}$$ _[2,3,4,6]_       
> $${\color{lightgreen}output:}$$ _8_  
> **Объяснение вывода:**  
> Для заданного примера возможно создание 8 кортежей:
> (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
> (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

   
# 3. **Что делает check_mismatch?**        
   Пользователем задается список целых чисел, который первоначально должен состоять из чисел от 1 до n (шаг = 1), но по какой-то причине один из элементов в списке дублировался.  
   Функция проверяет какое именно число встречается дважды (a) и какое число пропущено (b)  
   в виде списка вида [a, b]. 

> [!NOTE]
> Пользователем задается $${\color{lightblue}один \space аргумент}$$ типа $${\color{lightblue}list}$$    
> $${\color{lightblue}Значение \space по \space умолчанию:}$$ _не задано_        

> [!TIP]
> **Пример ввода-вывода:**        
> $${\color{lightgreen}input:}$$ _[1, 2, 2, 4]_       
> $${\color{lightgreen}output:}$$ _[2, 3]_
