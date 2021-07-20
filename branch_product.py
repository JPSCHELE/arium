

class ProductBranch:
    def __init__(self, id, store_id, ean, branch):
        self.id = id
        self.store_id = store_id
        self.ean = ean
        self.branch = branch
        self.stock = 0
        self.last_update = "NA"

    def __repr__(self):
        return str(self.id)+" "+self.branch

