from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

from django.db.models import Prefetch
from django.db.models import QuerySet

from cdb.models import GlobalTag, GlobalTagStatus, GlobalTagType, PayloadList, PayloadType, PayloadIOV
# from todos.permissions import UserIsOwnerTodo
from cdb.serializers import GlobalTagCreateSerializer, GlobalTagReadSerializer, GlobalTagStatusSerializer, GlobalTagTypeSerializer
from cdb.serializers import PayloadListCreateSerializer, PayloadListReadSerializer, PayloadTypeSerializer
from cdb.serializers import PayloadIOVSerializer

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
        #print(queryset[0].status)
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


class PayloadListListCreationAPIView(ListCreateAPIView):
    #    authentication_classes = ()
    #    permission_classes = ()
    serializer_class = PayloadListCreateSerializer

    def get_queryset(self):
        return PayloadList.objects.all()
        # return GlobalTag.objects.select_related('status').all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PayloadListReadSerializer(queryset, many=True)
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

class PayloadTypeListCreationAPIView(ListCreateAPIView):
    #    authentication_classes = ()
    #    permission_classes = ()
    serializer_class = PayloadTypeSerializer

    def get_queryset(self):
        return PayloadType.objects.all()
        # return GlobalTag.objects.select_related('status').all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PayloadTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data)

class PayloadIOVListCreationAPIView(ListCreateAPIView):
    #    authentication_classes = ()
    #    permission_classes = ()
    serializer_class = PayloadIOVSerializer

    def get_queryset(self):
        return PayloadIOV.objects.all()
        # return GlobalTag.objects.select_related('status').all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PayloadIOVSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

class PayloadIOVsListAPIView(ListAPIView):

        def get_queryset(self):

            globalTagId = self.kwargs.get('globalTagId')
            majorIOV = self.kwargs.get('majorIOV')
            minorIOV = self.kwargs.get('minorIOV')

            plists = PayloadList.objects.filter(global_tag__id=globalTagId)
            piov_ids = []
            for pl in plists:
                #print(pl)
                piov = PayloadIOV.objects.filter(payload_list = pl, major_iov__lte = majorIOV,minor_iov__lte=minorIOV)
                if piov:
                    piov=piov.latest('major_iov','minor_iov')
                    #print(piov)
                    piov_ids.append(piov.id)

            #print(piov_ids)

            piov_querset = PayloadIOV.objects.filter(id__in=piov_ids)

            return PayloadList.objects.filter(global_tag__id=globalTagId).prefetch_related(Prefetch(
                  'payload_iov',
                  queryset=piov_querset
                  )).filter(payload_iov__in=piov_querset).distinct()


        def list(self, request, globalTagId, majorIOV, minorIOV ):

            queryset = self.get_queryset()
            serializer = PayloadListReadSerializer(queryset, many=True)
            return Response(serializer.data)