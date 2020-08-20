def get_size(w,h,d):
    return [((w*h)+(w*d)+(h*d))*2, w * h * d]

print(get_size(6,4,2))

'''
Write a function that returns the total surface area and volume of a box as an array: [area, volume].
'''