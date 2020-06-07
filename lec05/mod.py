def safe_sum(a,b):
    if type(a) !=type(b):
        print ("같은 타입이 아닙니다.")
        return;
    else:
        return a+b;

if __name__=='__main__': ##파일을 직접 실행시켰을때만 실행됨
    print("just print")