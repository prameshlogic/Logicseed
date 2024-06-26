
# while True:
#     try:
#         # Read user input
#         user = input('>>> ')
        

#         if user.strip().lower() in ['exit', 'quit']:
#             print("Exiting REPL. Goodbye!")
#             break

#         try:
#             result = eval(user)
#             if result is not None:
#                 print(result)
#         except SyntaxError:
#             exec(user)
#     except (EOFError, KeyboardInterrupt):
#         print("\nExiting REPL. Goodbye!")
#         break
#     except Exception as e:
#         print(f"Error: {e}")

while True:
    try:
        user = input('>>> ')

        try:
            rs = eval(user)
            if rs is not None:
                print(rs)
        except SyntaxError:
            ne=exec(user)
    except (EOFError, KeyboardInterrupt):
        print("\nExiting REPL. Goodbye!")
        break
    except Exception as e:
        print(f"Error:{e}")        