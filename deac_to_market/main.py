import random
import threading
import time

import config
import market

def update_items():
	if not config.bump:
		return
	while True:
		try:
			#print "Removing items"
			#market_items = market.inventory(-2)
			#for market_item in market_items:
				#print "Removing %s" % market_item["name"]
				#market.remove_from_market(market_item["id"])
				#time.sleep(2)

			deactivated_items = market.inventory()
			sorted_items = sorted(deactivated_items, key=lambda x: config.item_prices.get(x["name"], 0) + random.randint(1, 1000))
			print "Bumping items"
			for deactivated_item in sorted_items:
				#print deactivated_item["name"]
				#price = config.item_prices.get(deactivated_item["name"])
                                #print price
				#if price == None:
					#TODO: set price below other seller but not below our buy price
					#print "Selling %s for %i" % (deactivated_item["name"], price)
				price = market.selling_price(deactivated_item["name"])
				if deactivated_item["name"] == "Chronos Hair":
					price = 15
				if deactivated_item["name"] == "Chronos Force":
					price = 30
				if deactivated_item["name"] == "Chronos Blood":
					price = 20
				if deactivated_item["name"] == "Chronos DQ":
					price = 10
				if deactivated_item["name"] == "Chronos Grip":
					price = 10
				if deactivated_item["name"] == "Chronos Right Leg Motion Trail":
					price = 10
				if deactivated_item["name"] == "Chronos Right Hand Motion Trail":
					price = 10
				if deactivated_item["name"] == "Chronos Left Leg Motion Trail":
					price = 10
				if deactivated_item["name"] == "Chronos Left Hand Motion Trail":
					price = 10
				if deactivated_item["name"] == "Gladiator Right Leg Motion Trail":
					price = 10
				if deactivated_item["name"] == "Gladiator Right Hand Motion Trail":
					price = 10
				if deactivated_item["name"] == "Gladiator Left Leg Motion Trail":
					price = 10
				if deactivated_item["name"] == "Gladiator Left Hand Motion Trail":
					price = 10
				if deactivated_item["name"] == "Gladiator Hair":
					price = 15
				if deactivated_item["name"] == "Gladiator Force":
					price = 45
				if deactivated_item["name"] == "Gladiator Blood":
					price = 20
				if deactivated_item["name"] == "Gladiator DQ":
					price = 10
				if deactivated_item["name"] == "Gladiator Grip":
					price = 10
				if deactivated_item["name"] == "Orc Blood":
					price = 49
				if deactivated_item["name"] == "Music":
					price = 140
				if deactivated_item["name"] == "Orc Hair":
					price = 30
				if deactivated_item["name"] == "Orc Right Leg Motion Trail":
					price = 20
				if deactivated_item["name"] == "Orc Right Hand Motion Trail":
					price = 20
				if deactivated_item["name"] == "Orc Left Leg Motion Trail":
					price = 20
				if deactivated_item["name"] == "Orc Left Hand Motion Trail":
					price = 20
				if deactivated_item["name"] == "Orc Force":
					price = 110
				if deactivated_item["name"] == "Orc Relax":
					price = 70
				if deactivated_item["name"] == "Chronos Primary Gradient":
					price = 15
				if deactivated_item["name"] == "Chronos Secondary Gradient":
					price = 15
				if deactivated_item["name"] == "Gladiator Primary Gradient":
					price = 15
				if deactivated_item["name"] == "Gladiator Secondary Gradient":
					price = 15
				if deactivated_item["name"] == "Acid Blood":
					price = 0
                                if deactivated_item["name"] == "Organic Cucumber":
					price = 0
                                if deactivated_item["name"] == "Pickled Cucumbers":
					price = 0
                              #  if 'Texture' in str(deactivated_item["name"]):
                              #          price = 0
       				if deactivated_item["name"] == "Head Texture":
					price = 220
				if 'Bumpmap' in str(deactivated_item["name"]):
					price = 2000
                               # if 'Chronos' not in str(deactivated_item["name"]) and 'Gladiator' not in str(deactivated_item["name"]):
                              #          price = 0
					
				if price > 0:
					if price < 10:
						price = 10
					print "Selling %s for %i" % (deactivated_item["name"], price-1)
					market.sell(deactivated_item["id"], price-1)
				time.sleep(2)	 
				#else:
					#print deactivated_item["name"], "has no priice, remove it"
				#time.sleep(1)
			time.sleep(config.bump_time)
		except Exception as e:
			print e


		"""for item, value in config.buy_items.iteritems():
			try:
				search = market.search(item, value)
				buy = [i for i in search if i["item_price"] <= value]
				print "Checking %s for %i (found %i)" % (item, value, len(buy))
				for buy_item in buy:
					print "Buying %s for %i" % (item, buy_item["item_price"])
					market.buy(buy_item)
			except Exception as e:
				print e"""
		#time.sleep(300)

update_t = threading.Thread(target=update_items)
update_t.daemon = True
update_t.start()

#check_t = threading.Thread(target=check_items)
#check_t.daemon = True
#check_t.start()

while True:
	try:
		print "tc: %s" % market.tc(config.username)
	except:
		pass
	time.sleep(config.show_tc_every)
	"""if last_item_update + update_items_every < time.time():
		last_item_update = time.time()



	if last_item_check + check_items_every < time.time():
		last_item_check = time.time()
		

	time.sleep(10)"""
