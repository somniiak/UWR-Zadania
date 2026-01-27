from parser import parser

args = parser.parse_args()

if args.mode == "local":
    import data_local as data
else:
    import data_api as data

if args.type == "books":
    if args.action == "add":
        print(data.books_add(args.author, args.title, args.year))

    elif args.action == "list":
        for line in data.books_list():
            print(line)

elif args.type == "people":
    if args.action == "add":
        print(data.people_add(args.name, args.email))

    elif args.action == "list":
        for line in data.people_list():
            print(line)

elif args.type == "loans":
    if args.action == "borrow":
        print(data.loans_borrow(args.book_id, args.person_id))

    elif args.action == "return":
        print(data.loans_return(args.loan_id))

    elif args.action == "list":
        for line in data.loans_list():
            print(line)
