from apscheduler.schedulers.blocking import BlockingScheduler
import os
import scraper
import helper

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=120)
def fetch_data():
  print("Fetching data")
  se_data = scraper.get_all_data_for('se')
  te_data = scraper.get_all_data_for('te')
  be_data = scraper.get_all_data_for('be')

  print("Removing old files")
  os.remove('data/se_data.pkl')
  os.remove('data/te_data.pkl')
  os.remove('data/be_data.pkl')

  print("Serializing fetched data to files")
  helper.serialize_to_file('se_data', se_data)
  helper.serialize_to_file('te_data', te_data)
  helper.serialize_to_file('be_data', be_data)

sched.start()
