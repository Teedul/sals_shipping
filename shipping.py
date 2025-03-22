# Define weight variable and set it equal to any number.
weight = 80


# Define flat charges for shipping
ground_shipping_flat_charge = 20.00
ground_shipping_flat_charge_premium = 125.00
print("Flat charge information:")
print("The flat charge for ground shipping is: " , ground_shipping_flat_charge)
print("The flat charge for ground shipping premium is: " , ground_shipping_flat_charge_premium)
print("There is no flat charge when drone shipping is selected.")
print("---------")


# Define ground shipping based on weight
if weight <= 2:
  cost = (weight * 1.50) + ground_shipping_flat_charge
elif weight > 2 and weight <= 6:
  cost = (weight * 3.00) + ground_shipping_flat_charge
elif weight > 6 and weight <= 10:
  cost = (weight * 4.00) + (ground_shipping_flat_charge)
elif weight > 10: 
  cost = (weight * 4.75) + ground_shipping_flat_charge
else:
  print("The weight entered caused an issue. Please enter a positive number")


# Drone shipping, no flat charges
if weight <= 2:
  cost_drone = (weight * 4.50)
elif weight > 2 and weight <= 6:
  cost_drone = (weight * 9.00)
elif weight > 6 and weight <= 10:
  cost_drone = (weight * 12.00)
elif weight > 10: 
  cost_drone = (weight * 14.75)
else:
  print("The weight entered caused an issue. Please enter a positive number")


  # Output cost based on the weight entered
print("Weight provided:", weight , "LBS")
print("For ground shipping:", cost)
print("For drone shipping:", cost_drone)


# Determine cheapest method
if cost < cost_drone and cost < ground_shipping_flat_charge_premium:
  print("Ground shipping is the cheapest method.")
elif cost_drone < cost and cost_drone < ground_shipping_flat_charge_premium:
  print("Drone shipping is the cheapest method.")
else:
  print("Ground shipping premium is the cheapest method.")
