import grpc
import calculator_grpc_pb2
import calculator_grpc_pb2_grpc


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:8081')
    client = calculator_grpc_pb2_grpc.apiStub(channel)

    while True:
        print('Enter 1 to add,'
              ' 2 to subtract,'
              ' 3 to multiply,'
              ' 4 to divide, 5 to exit')
        print()
        n = input('Enter your choice: ')
        if n == '1':
            print('Welcome to Addition')
            x = int(input('Enter First num:'))
            y = int(input('Enter Second num:'))
            res = client.add(calculator_grpc_pb2.twoNums(numOne=x, numTwo=y))
            print(res.num)
        elif n == '2':
            print('Welcome to Subtraction')
            x = int(input('Enter First num:'))
            y = int(input('Enter Second num:'))
            res = client.sub(calculator_grpc_pb2.twoNums(numOne=x, numTwo=y))
            print(res.num)
        elif n == '3':
            print('Welcome to Multiplication')
            x = int(input('Enter First num:'))
            y = int(input('Enter Second num:'))
            res = client.mul(calculator_grpc_pb2.twoNums(numOne=x, numTwo=y))
            print(res.num)
        elif n == '4':
            print('Welcome to Division')
            x = int(input('Enter First num:'))
            y = int(input('Enter Second num:'))
            res = client.div(calculator_grpc_pb2.twoNums(numOne=x, numTwo=y))
            print(res.num)
        elif n =='5':
            print('Exiting')
            exit()
        else:
            print('Invalid Input,')
