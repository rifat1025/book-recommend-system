from django.shortcuts import render
import pickle
import numpy as np

# load pickle
popular = pickle.load(open('picklefile/popularity_df', 'rb'))
pt = pickle.load(open('picklefile/pt.pkl', 'rb'))
books_df = pickle.load(open('picklefile/books.pkl', 'rb'))
similarity_scores = pickle.load(open('picklefile/similarity_scores.pkl', 'rb'))
print(popular.head())


def index(request):
    # convert popular DataFrame to list of dicts
    books_list = popular.to_dict('records')

    # optional: clean column names
    popular.columns = popular.columns.str.strip()

    for book in books_list:
        book['title'] = book.get('Book-Title', 'No Title')
        book['author'] = book.get('Book-Author', 'Unknown')
        book['publisher'] = book.get('Publisher', 'Unknown')
        book['rating'] = book.get('avg_rating', 0)
        book['votes'] = book.get('num_ratings', 0)
        img = book.get('Image-URL-M')
        if img:
            img = img.replace('http://', 'https://')
        book['image'] = img or 'https://via.placeholder.com/250x300'

    return render(request, 'system/index.html', {'books': books_list})

def recommend(request):
    user_input = request.POST.get('search')

    if user_input not in pt.index:
        return render(request, 'system/reommend.html', {'data': [], 'error': f"Book '{user_input}' not found!"})

    book_idx = int(np.where(pt.index == user_input)[0][0])

    sim_scores = list(enumerate(similarity_scores[book_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:7]

    data = []
    for i in sim_scores:
        idx = i[0]
        title = pt.index[idx]
        temp_df = books_df[books_df['Book-Title'] == title].drop_duplicates('Book-Title')

        if temp_df.empty:
            continue

        book_data = {
            'title': temp_df['Book-Title'].values[0],
            'author': temp_df['Book-Author'].values[0],
            'publisher': temp_df['Publisher'].values[0] if 'Publisher' in temp_df else 'Unknown',
            'rating': temp_df['avg_rating'].values[0] if 'avg_rating' in temp_df else 0,
            'votes': temp_df['num_ratings'].values[0] if 'num_ratings' in temp_df else 0,
            'image': temp_df['Image-URL-M'].values[0] if temp_df['Image-URL-M'].values[0] else 'https://via.placeholder.com/250x300'
        }
        data.append(book_data)

    return render(request,'system/reommend.html', {'data': data})