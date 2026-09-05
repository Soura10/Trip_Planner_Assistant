from tools.tavily import tavily_search
from tools.flight_tool import search_flights

#res = tavily_search("Best hotels in Bangalore")
#print(res)

res = search_flights("plan a trip from kolkata to bangalore for 7 days")
print(res)

