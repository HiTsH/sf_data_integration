from sf_data_integration import SalesforceConnector, DataIntegrator, DataTracker, setup_logger

def run_integration():
    project_name = "salesforce_project"
    logger = setup_logger(project_name)

    sf_credentials = {
        "username": "your_username",
        "password": "your_password",
        "security_token": "your_security_token"
    }
    source_files = ["data/source_file_1.csv"]
    object_name = "Account"

    sf_conn = SalesforceConnector(**sf_credentials, logger=logger)
    integrator = DataIntegrator(source_files)
    tracker = DataTracker(f"{project_name}_tracking.csv")

    data = integrator.load_data()
    cleaned_data = integrator.clean_data(data)
    transformed_data = integrator.transform_data(cleaned_data)

    new_data = []
    for record in transformed_data:
        record_hash = tracker.generate_hash(record)
        if not tracker.is_migrated(record_hash):
            new_data.append(record)
            tracker.track_migration(record_hash)

    if new_data:
        sf_conn.insert_records(object_name, new_data)
        tracker.save_tracking()

if __name__ == "__main__":
    run_integration()
