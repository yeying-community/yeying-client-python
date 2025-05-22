python3 -m grpc_tools.protoc -I ../yeying-idl \
        --python_out=./ \
        --pyi_out=./ \
        --grpc_python_out=./ \
        --init_python_out=./ \
        --init_python_opt=imports=protobuf+grpcio \
        ../yeying-idl/yeying/api/**/*.proto


python3 -m grpc_tools.protoc -I ../yeying-idl \
        --python_out=./ \
        --pyi_out=./ \
        --grpc_python_out=./ \
        --init_python_out=./ \
        --init_python_opt=imports=protobuf+grpcio \
        ../yeying-idl/yeying/api/apps/zuoyepigai/*.proto