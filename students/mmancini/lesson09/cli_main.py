#!/usr/bin/env python3


from donor_models import Donor
from donor_models import DonorCollection

###################################

global canned_sorted_report
global canned_thankyou_email
global canned_all_donors_listed

charity_name = "ABC Charity"

all_donors = DonorCollection()

# db_donors2 = {
#             "Jane Smith": [25, 50],
#             "Tom Adams": [100],
#             "Helen Smalls": [10, 20, 30],
#             "Ming Chan": [50],
#             "Mary Jones": [5, 10, 15]}

###################################


def init():
    global canned_sorted_report
    global canned_thankyou_email
    global canned_all_donors_listed
    canned_sorted_report = "canned_sorted_report.txt"
    canned_thankyou_email = "canned_thankyou_email.txt"
    canned_all_donors_listed = "canned_all_donors_listed.txt"


def read_file(in_filespec):
    with open(in_filespec, "r") as f:
        data = f.read()
    return data


def write_file(in_filespec, in_msg):
    with open(in_filespec, "w") as f:
        f.write(in_msg)


def display_donors(in_dict_all_donors):
    hdr_listed_donors = f"List of Donors:"
    listed_donors = hdr_listed_donors + "\n" + str((f" ", *in_dict_all_donors.keys()))
    print(listed_donors)
    # write_file(canned_all_donors_listed, listed_donors)
    return listed_donors


def get_all_donors():
    return all_donors


def get_donor_stats(in_donor, in_dict_all_donors):
    stats_ary = []

    donations_ary = in_dict_all_donors[in_donor]

    num_donations = len(donations_ary)
    tot_of_donations = sum(donations_ary)
    avg_of_donations = tot_of_donations / num_donations

    stats_ary.append(tot_of_donations)
    stats_ary.append(num_donations)
    stats_ary.append(avg_of_donations)

    # print("fstats={}",stats_ary)
    return stats_ary


def send_thankyou_email(in_name, in_amount):
    print(f"Thank You Email:")

    dict_data_line = {"donor_name": in_name, "donation_amount": float(in_amount)}

    msg = ""
    msg += f"To: {in_name}@abc.def:\n"

    msg += f"From: {charity_name}.org:\n"
    msg += f"Subject:  Thank You:\n"
    msg += f"Body: Dear {in_name} Thank You for your generous donation of ${in_amount}:\n".format(**dict_data_line)
    msg += ""

    # write_file(canned_thankyou_email, msg)
    print(msg)
    return msg


###################################

def process_donor_donation(name, amount):
    all_donors.add_donation(name, amount)
    print(f"donor {name} donated {amount}")
    email = send_thankyou_email(name, amount)
    return email


###################################

# ui Menus

def ui_menu_main():
    msg = ""
    msg += "Please enter option from below:\n"
    msg += " D: Receive donation\n"
    msg += " L: Display list of donors\n"
    msg += " S: Send thank you email\n"
    msg += " R: Create report\n"
    msg += " W: Write letters to all\n"
    msg += " Q: Quit\n"
    msg += ".....>>"

    # ***MMM entry = input(msg)
    # entry = 'R'
    # entry = 'W'
    entry = 'L'

    return entry


def ui_menu_specify_donor_name():
    msg = ""
    msg += "Please enter donor name :\n"
    msg += ".....>>"

    entry = input(msg)

    return entry


def ui_menu_specify_donation_amount():
    msg = ""
    msg += "Please enter a donation amount::\n"
    msg += ".....>>"

    donation_amount_entry = int(input(msg))

    return donation_amount_entry


###################################

# Operations

def op_receive_donation():
    pass
    donor_name = ui_menu_specify_donor_name()
    donation_amount = ui_menu_specify_donation_amount()
    process_donor_donation(donor_name, donation_amount)


def op_display_list_of_donors():
    display_donors(all_donors.dict_donors)
    pass

# def show_donors():
#     hdr_listed_donors = f"List of Donors:"
#     listed_donors = hdr_listed_donors + "\n" + str((f" ", *db_donors.keys()))
#     print(listed_donors)
#     #write_file(canned_all_donors_listed, listed_donors)
#     return listed_donors


# def op_create_report(in_dict_donors_db):
#
#     print(f"Donor Report:")
#
#     # sort donors report by total donation
#     db2 = []
#     for donor in in_dict_donors_db:
#         donor_stats = get_donor_stats(donor,in_dict_donors_db)
#         tup = (donor,)
#         tup += (donor_stats[1],)
#         tup += (donor_stats[2],)
#         db2.append((donor_stats[0], tup))
#     db2.sort(reverse=True)
#
#     hdr1 = ["Donor Name ", "Donation Total", "Number of Donations", "Donation Average"]
#     hdr2 = ["-----------", "--------------", "-------------------", "----------------"]
#
#     print("   {: <20} {: >20} {: >20} {: >20}".format(*hdr1))
#     print("   {: <20} {: >20} {: >20} {: >20}".format(*hdr2))
#
#     # for key, value in db_donors2.items():
#     for donor_info in db2:
#
#         tup_info = donor_info[1]
#         rpt_donation_line = {"donor_name": tup_info[0], "donation_total": donor_info[0],
#                              "number_of_donations": tup_info[1],
#                              "donation_average": tup_info[2]}
#         print("   {donor_name: <20} {donation_total: >20} {number_of_donations: >20} "
#                   "{donation_average: >20}".format(**rpt_donation_line))
#
#     # write_file(canned_sorted_report, report)


def op_create_report(in_dict_donors_db):
    print(f"Donor Report:")

    # sort donors report by total donation
    db2 = []
    for donor in in_dict_donors_db:
        donor_stats = get_donor_stats(donor, in_dict_donors_db)
        tup = (donor,)
        tup += (donor_stats[1],)
        tup += (donor_stats[2],)
        db2.append((donor_stats[0], tup))
    db2.sort(reverse=True)

    hdr1 = ["Donor Name ", "Donation Total", "Number of Donations", "Donation Average"]
    hdr2 = ["-----------", "--------------", "-------------------", "----------------"]

    hdrline1 = ("   {: <20} {: >20} {: >20} {: >20}".format(*hdr1)) + "\n"
    hdrline2 = ("   {: <20} {: >20} {: >20} {: >20}".format(*hdr2)) + "\n"

    rptlines = ""
    # for key, value in db_donors2.items():
    for donor_info in db2:

        tup_info = donor_info[1]
        rpt_donation_line = {"donor_name": tup_info[0], "donation_total": donor_info[0],
                             "number_of_donations": tup_info[1],
                             "donation_average": tup_info[2]}
        rptlines += ("   {donor_name: <20} {donation_total: >20} {number_of_donations: >20} "
                     "{donation_average: >20}".format(**rpt_donation_line)) + "\n"

    report = hdrline1 + hdrline2 + rptlines
    # write_file(canned_sorted_report, report)
    print(report)
    return report


def op_write_letters_to_all(in_dict_donors_db):

    for key, value in in_dict_donors_db.items():

        donor_name = key
        donations_ary = value
        donations_total = sum(donations_ary)

        filename = donor_name + ".txt"
        with open(filename, "w") as f:
            dict_data_line = {"donor_name": donor_name, "donation_amount": float(donations_total)}
            thank_you_letter = ""
            thank_you_letter += f"Dear {donor_name} Thank You for your generous donations " \
                                f"totaling ${donations_total}:\n".format(**dict_data_line)
            f.write(thank_you_letter)


def op_done():
    print("mailroom end")
    quit()


###################################

init()


def mailroom_main():
    print("mailroom begin")

    op_action_dict = {
                    'D': op_receive_donation,
                    'L': op_display_list_of_donors,
                    'R': op_create_report,
                    'W': op_write_letters_to_all,
                    'Q': op_done
                     }

    while True:
        operation = ui_menu_main()
        op_action_dict.get(operation)()




