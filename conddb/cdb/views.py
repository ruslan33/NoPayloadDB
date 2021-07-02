from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

from cdb.models import GlobalTag, GlobalTagStatus, GlobalTagType
# from todos.permissions import UserIsOwnerTodo
from cdb.serializers import GlobalTagCreateSerializer, GlobalTagReadSerializer, GlobalTagStatusSerializer, GlobalTagTypeSerializer


class GlobalTagDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GlobalTagReadSerializer
    queryset = GlobalTag.objects.all()
 #   permission_classes = (IsAuthenticated, UserIsOwnerTodo)

class GlobalTagListCreationAPIView(ListCreateAPIView):


#    authentication_classes = ()
#    permission_classes = ()
    serializer_class = GlobalTagCreateSerializer


    def get_queryset(self):
        return GlobalTag.objects.all()
        #return GlobalTag.objects.select_related('status').all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        print(queryset[0].status)
        serializer = GlobalTagReadSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # gt= serializer.instance
        # globaltag = GlobalTag.objects.get_or_create(gt)
        # data = serializer.data
        # data["globaltag"] = token.key

        # headers = self.get_success_headers(serializer.data)
        return Response(serializer.data)
        # return Response(status=status.HTTP_201_CREATED)

class GlobalTagStatusCreationAPIView(ListCreateAPIView):


#    authentication_classes = ()
#    permission_classes = ()
    serializer_class = GlobalTagStatusSerializer


    def get_queryset(self):
        return GlobalTagStatus.objects.all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = GlobalTagStatusSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)


        # headers = self.get_success_headers(serializer.data)
        return Response(serializer.data)


class GlobalTagTypeCreationAPIView(ListCreateAPIView):


#    authentication_classes = ()
#    permission_classes = ()
    seriaserializer_class = GlobalTagTypeSerializerlizer_class = GlobalTagTypeSerializer


    def get_queryset(self):
        return GlobalTagType.objects.all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = GlobalTagTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)


        # headers = self.get_success_headers(serializer.data)
        return Response(serializer.data)