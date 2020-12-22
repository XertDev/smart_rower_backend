class AlreadyExistError(RuntimeError):
	def __init__(self, *args):
		super(AlreadyExistError).__init__(*args)
