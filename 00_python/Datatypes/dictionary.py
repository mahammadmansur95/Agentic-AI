chai_order = dict(type="chai", size="Large", sugar=2)
print("chai", chai_order)

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print("chai recipe :", chai_recipe)
del chai_recipe["liquid"]
print("chai recipe :", chai_recipe)

print("keys() :", chai_order.keys())
print("values() :", chai_order.values())
print("items() :", chai_order.items())

last_item = chai_order.popitem()
print("lastitem using popitem() : ", last_item)

extend = {"name": 'mansur'}
chai_recipe.update(extend)
print("chai receipe update :", chai_recipe)

isSizePresent = chai_order.get("size", 'no size');

print("isSizePresent size :", isSizePresent)