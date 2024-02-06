class MyPipeline:
    def process_item(self, item, spider):
        data_dict = dict(item)
        return data_dict