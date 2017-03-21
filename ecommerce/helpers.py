import math

from .apps import EcommerceConfig

class Helpers():
	
	def get_path(file):
		module_name = EcommerceConfig.name
		
		return '/' + module_name + '/' + file
		
	def get_url(file):
		module_name = EcommerceConfig.name
		
		return module_name + '/' + file
		
	def nagivation_list(count, per_page, cur_page):
		pagination_nav = ""
		previous_btn = True
		next_btn = True
		first_btn = True
		last_btn = True
			
		no_of_paginations = int(math.ceil(count / per_page))
		
		if cur_page >= 7:
			start_loop = cur_page - 3
			if no_of_paginations > cur_page + 3:
				end_loop = cur_page + 3
			elif cur_page <= no_of_paginations and cur_page > no_of_paginations - 6:
				start_loop = no_of_paginations - 6
				end_loop = no_of_paginations
			else:
				end_loop = no_of_paginations
		else:
			start_loop = 1
			if no_of_paginations > 7:
				end_loop = 7
			else:
				end_loop = no_of_paginations

		# Pagination Buttons logic     
		pagination_nav += "<div class='pagination-container'><ul>"

		if first_btn and cur_page > 1:
			pagination_nav += "<li p='1' class='active'>First</li>"
		elif first_btn:
			pagination_nav += "<li p='1' class='inactive'>First</li>"

		if previous_btn and cur_page > 1:
			pre = cur_page - 1
			pagination_nav += "<li p='" + str(pre) + "' class='active'>Previous</li>"
		elif previous_btn:
			pagination_nav += "<li class='inactive'>Previous</li>"
		
		for i in range(start_loop, end_loop + 1):
			if cur_page == i:
				pagination_nav += "<li p='" + str(i) + "' class = 'selected'>" + str(i) + "</li>"
			else:
				pagination_nav += "<li p='" + str(i) + "' class='active'>" + str(i) + "</li>"

		if next_btn and cur_page < no_of_paginations:
			nex = cur_page + 1
			pagination_nav += "<li p='" + str(nex) + "' class='active'>Next</li>"
		elif next_btn:
			pagination_nav += "<li class='inactive'>Next</li>"

		if last_btn and cur_page < no_of_paginations:
			pagination_nav += "<li p='" + str(no_of_paginations) + "' class='active'>Last</li>"
		elif last_btn:
			pagination_nav += "<li p='" + str(no_of_paginations) + "' class='inactive'>Last</li>"

		pagination_nav = pagination_nav + "</ul></div>"
		
		return pagination_nav