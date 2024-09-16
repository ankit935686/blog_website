from datetime import date
from django.shortcuts import render 

all_posts= [
    {
        "slug":"into-the-woods",
        "image":"woods.jpg",
        "date":date(2024, 7, 21),
        "title": "into-woods",
        "excerpt":"there is nothin like the views you get when hiking in the mountains ",
        "content":""""" Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
        
         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
        
         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
        
        
        """
               
        
        
    },
    
    
     {
        "slug":"hike-in-in-the-mountains",
        "image":"coding.jpg",
        "date":date(2024, 9, 11),
        "title": "programming-is-fun",
        "excerpt":"there is nothin like the views you get when hiking in the mountains ",
        "content":""""" Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
        
         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
        
         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
        
        
        """
     },
     
      {
        "slug":"programming-is-fun",
        "image":"moutains.jpg",
        "date":date(2024, 9, 7),
        "title": "mountain hiking",
        "excerpt":"there is nothin like the views you get when hiking in the mountains ",
        "content":""""" Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
        
         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
        
         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, neque exercitationem non sunt doloribus, quas,
        maiores fugiat pariatur repudiandae nulla quae laborum. Cum fuga quidem facere maiores expedita blanditiis eum!
        
        
        """
      }              
    
]



def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts =sorted(all_posts,key=get_date)
    latest_posts =sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts": latest_posts
    })



      
def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts":all_posts
    })

def post_details(request,slug):
   return render(request, "blog/post-detail.html")
