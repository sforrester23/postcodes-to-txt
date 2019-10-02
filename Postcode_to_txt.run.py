from Postcode_to_txt_define import *

# postcode_dictionary = postcode_to_json('TN279SF', 'http://api.postcodes.io/postcodes/')
postcode_dictionary = postcode_to_json('TN279SF', 'http://api.postcodes.io/postcodes/')
postcode_text = postcode_to_text('TN279SF', 'http://api.postcodes.io/postcodes/')
postcode_status_code = postcode_status_request('TN279SF', 'http://api.postcodes.io/postcodes/')

random_postcode_dictionary = postcode_to_json('', 'http://api.postcodes.io/random/postcodes')
random_postcode_text = postcode_to_text('', 'http://api.postcodes.io/random/postcodes')
random_postcode_status_code = postcode_status_request('', 'http://api.postcodes.io/random/postcodes')

# Test set up, print the values so we can see them
print(postcode_dictionary)
print(postcode_text)
print(postcode_status_code)

try:
    thing_to_write = postcode_dictionary['result']
    # print(thing_to_write.keys())
    for item in thing_to_write:
        write_to_file('postcode.txt', item + ': ' + str(thing_to_write[item]))

    write_to_file('postcode.txt', '\n')

    thing_to_write = random_postcode_dictionary['result']
    # print(thing_to_write.keys())
    for item in thing_to_write:
        write_to_file('postcode.txt', item + ': ' + str(thing_to_write[item]))

except KeyError as KeyErr:
    print('That Key is producing an error, making it hard to write the file. Could the postcode be incorrect?')

finally:
    print('Execution completed. \n')