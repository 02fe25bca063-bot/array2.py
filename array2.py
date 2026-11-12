def main():
 scores = [78,82,65,92]
 total = sum(scores)
 avg = total / len(scores)
 print("===main / master branch output===")
 print(f"scores:{scores}")
 print(f"sum:{total}")
 print(f"Average:{avg}")
 print("\n ==local branch output(max&min)===")
 print(f"maximum : {max(scores)}")
 print(f"minimum : {min(scores)}")
if_name_="_main_"
main()