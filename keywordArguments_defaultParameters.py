def about(name,age,likes="java"): # here these are function-parameters!
        sentence="Meet {}! He is  {} yrs old and he likes {}".format(name,age,likes)
        print(sentence)
about("jack",23,"python")  # function-argument
# we pass the function-argument to the function and it takes up and  function parameters takes them and do the work!!
'''
The parameter is what we use in the function definition.
So, the parameters in this case would be name,age,likes.
But,the arguments are what we actually pass to the function or what we give
to the function when we call it.
So,here our arguments are Jack,23,python.
The argument jack matches to the parameter name,23 to age and python with likes.
and teh reason it does that is because we types them in a specific order.
But we can't enter arguments in any order we like as long as we make it clear
which parameter they associate with and when we do that they become keyword arguments.
--->> If we provide with keyword-arguments then order does not matter.
--->> provide default value and if the function doesnot get value from argument then it will take that
--->> otherwise print the value provided in keyword-argument
--->> default values must be defined in the last
'''
about(age=24,name="Priyanka",likes="Book-Reading")
about(age=23,name="Satyam")


