ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = ft_tuple[:1] + ("Brasil!",)

ft_set = ft_set.difference({"tutu!"})
ft_set.update({"Sao Paulo!"})


ft_dict["Hello"] = "42 Sao Paulo!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
