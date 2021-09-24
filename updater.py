from apscheduler.schedulers.blocking import BlockingScheduler
import scraper
import helper

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=120)
def fetch_data():
    se_data = scraper.get_all_data_for('se')
    te_data = scraper.get_all_data_for('te')
    be_data = scraper.get_all_data_for('be')

    helper.serialize_to_file('se_data', se_data)
    helper.serialize_to_file('te_data', te_data)
    helper.serialize_to_file('be_data', be_data)

sched.start()
