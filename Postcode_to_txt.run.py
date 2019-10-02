from Postcode_to_txt_define import *

# postcode_dictionary = postcode_to_json('TN279SF', 'http://api.postcodes.io/postcodes/')
postcode_dictionary = postcode_to_json('T279SF', 'http://api.postcodes.io/postcodes/')
postcode_text = postcode_to_text('TN279SF', 'http://api.postcodes.io/postcodes/')
postcode_status_code = postcode_status_request('TN279SF', 'http://api.postcodes.io/postcodes/')


print(postcode_dictionary)
print(postcode_text)
print(postcode_status_code)

thing_to_write = postcode_dictionary['result']
print(thing_to_write.keys())
for item in thing_to_write:
    write_to_file('postcode.txt', item + ': ' + str(thing_to_write[item]))

