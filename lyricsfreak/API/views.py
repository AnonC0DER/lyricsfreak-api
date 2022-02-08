from rest_framework.response import Response
from rest_framework.decorators import api_view
from API.serializers import Get_lyrics


@api_view(['GET'])
def AllMethods(request):
    routes = [
        {'GET' : '/search-lyrics/query'},
    ]
    
    return Response(routes)


@api_view(['GET'])
def Lyrics(request, q):
    '''Enter music and artist name to get the lyrics'''
    query = q

    lyrics = Get_lyrics(query)

    return Response(lyrics)