from src.models.operation_manager import OperationManager
from src.models.data_populator import populate_user_data

if __name__=='__main__':
    app=OperationManager()
    populate_user_data(app)
    app.run()