from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Like, Recital,User,Juki,Comment,kamil
from .serializers import RecitalSerializer,UserSerializer,JukiSerializer,CommentSerializer,KamilSerializer,LikeSerializer



class UserView(APIView,UpdateModelMixin,DestroyModelMixin):
    def get(self,request,id=None):
        if id:

            try:
                queryset=User.objects.get(id=id)
            except User.DoesNotExist:
                return Response({'erreur': 'Cet utilisateur N existe Pas.'}, status=400)

            read_serializer=UserSerializer(queryset)
    
        else:

            queryset=User.objects.all()

            read_serializer=UserSerializer(queryset ,many=True)
    
        return Response(read_serializer.data)


    def post(self,request):
        
            create_serializer=UserSerializer(data=request.data)

            if create_serializer.is_valid():

                User_item_object = create_serializer.save()

                read_serializer = UserSerializer(User_item_object)

                return Response(read_serializer.data, status=201)
            
            return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
            User_item = User.objects.get(id=id)
        except User.DoesNotExist:

            return Response({'erreur': 'desole cet Utilisateur n existe pas.'}, status=400)


        update_serializer = UserSerializer(User_item, data=request.data)


        if update_serializer.is_valid():


            User_item_object = update_serializer.save()


            read_serializer = UserSerializer(User_item_object)


            return Response(read_serializer.data, status=200)


        return Response(update_serializer.errors, status=400)

    def delete(self, request, id=None):
        try:

            User_item = User.objects.get(id=id)

        except User.DoesNotExist:

            return Response({'erreur': 'Cet utilisateur n exite pas.'}, status=400)

        User_item.delete()

        return Response(status=204)
        


class RecitalView(APIView,UpdateModelMixin,DestroyModelMixin):
    def get(self,request,id=None):
        if id:

            try:
                queryset=Recital.objects.get(id=id)
                jukyTaked=Juki.objects.filter(fromRecital=id)
                thekamil=kamil.objects.all()
            except Recital.DoesNotExist:
                return Response({'erreur': 'Ce recital N existe Pas.'}, status=400)
            
            if jukyTaked:
                read_serializerJuki=JukiSerializer(jukyTaked,many=True)
                read_serializer=RecitalSerializer(queryset)
                read_serializerKamil=KamilSerializer(thekamil,many=True)
                response=[read_serializer.data,read_serializerJuki.data,read_serializerKamil.data]

            read_serializerJuki=JukiSerializer(jukyTaked,many=True)
            read_serializer=RecitalSerializer(queryset)
            read_serializerKamil=KamilSerializer(thekamil,many=True)
            response=[read_serializer.data,read_serializerJuki.data,read_serializerKamil.data]

        
        else:

            queryset=Recital.objects.filter(recitalType='PUBLIC')

            read_serializer=RecitalSerializer(queryset ,many=True)
            response=read_serializer.data


        
        return Response(response)


    def post(self,request):

        create_serializer=RecitalSerializer(data=request.data)

        if create_serializer.is_valid():

            Recital_item_object = create_serializer.save()

            read_serializer = RecitalSerializer(Recital_item_object)

            return Response(read_serializer.data, status=201)
        
        return Response(create_serializer.errors, status=400)



    def put(self, request, id=None):
        try:
            Recital_item = Recital.objects.get(id=id)
        except Recital.DoesNotExist:

            return Response({'erreur': 'desole ce recital n existe pas.'}, status=400)


        update_serializer = RecitalSerializer(Recital_item, data=request.data)


        if update_serializer.is_valid():


            Recital_item_object = update_serializer.save()


            read_serializer = RecitalSerializer(Recital_item_object)


            return Response(read_serializer.data, status=200)


        return Response(update_serializer.errors, status=400)




    def delete(self, request, id=None):
        try:

            Recital_item = Recital.objects.get(id=id)

        except Recital.DoesNotExist:

            return Response({'erreur': 'Ce recital n exite pas.'}, status=400)

        Recital_item.delete()

        return Response(status=204)




class JukiTakedView(APIView,UpdateModelMixin,DestroyModelMixin):


    def get(self,request,userid=None,recitalid=None):
        if userid and recitalid:

            try:
                queryset=Juki.objects.filter(chosedBy=userid).filter(fromRecital=recitalid)
            except Juki.DoesNotExist:
                return Response({'erreur': 'Cet utilisateur na participer a aucun recital.'}, status=400)

            read_serializer=JukiSerializer(queryset,many=True)
        
        elif userid  :
            try:
                queryset=Juki.objects.filter(chosedBy=userid)
            except Juki.DoesNotExist:
                return Response({'erreur': 'Cet utilisateur na participer a aucun recital.'}, status=400)

            read_serializer=JukiSerializer(queryset,many=True)


        else:

            queryset=Juki.objects.filter(fromRecital=recitalid)

            read_serializer=JukiSerializer(queryset ,many=True)

        
        return Response(read_serializer.data)


    def post(self,request):
      
        create_serializer=JukiSerializer(data=request.data)

        if create_serializer.is_valid():

            Juki_item_object = create_serializer.save()

            read_serializer = JukiSerializer(Juki_item_object)

            return Response(read_serializer.data, status=201)
        
        return Response(create_serializer.errors, status=400)

    def delete(self, request, id=None):
        try:

            Juki_item = Juki.objects.get(id=id)

        except Juki.DoesNotExist:

            return Response({'erreur': 'Ce Juki n exite pas.'}, status=400)

        Juki_item.delete()

        return Response(status=204)


class CommentsView(APIView,UpdateModelMixin,DestroyModelMixin):
    def get(self,request,id=None):
        if id:

            try:
                queryset=Comment.objects.get(id=id)
            except Comment.DoesNotExist:
                return Response({'erreur': 'Ce commetaire N existe Pas.'}, status=400)

            read_serializer=CommentSerializer(queryset)
        
        else:

            queryset=Comment.objects.all()

            read_serializer=CommentSerializer(queryset ,many=True)
        
        return Response(read_serializer.data)


    def post(self,request):

        create_serializer=CommentSerializer(data=request.data)

        if create_serializer.is_valid():

            Comment_item_object = create_serializer.save()

            read_serializer = CommentSerializer(Comment_item_object)

            return Response(read_serializer.data, status=201)
        
        return Response(create_serializer.errors, status=400)



    def delete(self, request, id=None):
        try:

            Comment_item = Comment.objects.get(id=id)

        except Comment.DoesNotExist:

            return Response({'erreur': 'Ce comentaire n exite pas.'}, status=400)

        Comment_item.delete()

        return Response(status=204)



class LikesView(APIView,UpdateModelMixin,DestroyModelMixin):
    def get(self,request,id=None):
        if id:

            try:
                queryset=Like.objects.count(theComment=id)
            except Like.DoesNotExist:
                return Response({'erreur': 'Ce Like N existe Pas.'}, status=400)

            read_serializer=LikeSerializer(queryset,many=True)
        
        return Response(read_serializer.data)


    def post(self,request):

        create_serializer=LikeSerializer(data=request.data)

        if create_serializer.is_valid():

            Like_item_object = create_serializer.save()

            read_serializer = LikeSerializer(Like_item_object)

            return Response(read_serializer.data, status=201)
        
        return Response(create_serializer.errors, status=400)



    def delete(self, request, id=None):
        try:

            Like_item = Like.objects.get(id=id)

        except Like.DoesNotExist:

            return Response({'erreur': 'Ce Like n exite pas.'}, status=400)

        Like_item.delete()

        return Response(status=204)



class theHollyCoranView(APIView,UpdateModelMixin,DestroyModelMixin):
    def get(self,request):
        
        queryset=kamil.objects.all()

        read_serializer=KamilSerializer(queryset ,many=True)
        
        return Response(read_serializer.data)
