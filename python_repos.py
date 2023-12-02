import requests
#make an api call and store the request
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github..v3.json'}
r=requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")
#store api responsein a variable
response_dict=r.json()
print(f"total repositories:{response_dict['total_count']}")
#explore information about the repositories
repo_dicts=response_dict['items']
print("repositories returned:{len(repo_dicts)}")
print("\nselected information about each repositories")
for repo_dict in repo_dicts:
	print(f"name:{repo_dict['name']}")
	print(f"owner:{repo_dict['owner']['login']}")
	print(f"stars:{repo_dict['stargazers_count']}")
	print(f"repository:{repo_dict['html_url']}")
	print(f"created:{repo_dict['created_at']}")
	print(f"updated:{repo_dict['updated_at']}")
	print(f"description:{repo_dict['description']}")
	
#examine the first repository
repo_dict=repo_dicts[0]
print('\nselected information about the first respository')
print(f"name:{repo_dict['name']}")
print(f"owner:{repo_dict['owner']['login']}")
print(f"stars:{repo_dict['stargazers_count']}")
print(f"repository:{repo_dict['html_url']}")
print(f"created:{repo_dict['created_at']}")
print(f"updated:{repo_dict['updated_at']}")
print(f"description:{repo_dict['description']}")

print(f"\nkeys:{len(repo_dict)}")
for key in sorted(repo_dict.keys()):
	print(key)
