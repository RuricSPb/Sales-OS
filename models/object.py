class Object:

    def __init__(
        self,
        id=None,

        # Основные данные
        name="",
        source="",
        external_id="",

        # Паспорт объекта ПСБ
        psb_id="",
        psb_link="",
        description="",

        region="",
        district="",
        address="",

        object_type="",
        work_type="",
        stage="",
        frame_type="",

        construction_period="",
        visit_date="",

        # Пользовательские поля
        customer="",
        contractor="",
        designer="",

        manager="",
        status="",
        comment=""
    ):

        self.id = id

        # Основные
        self.name = name
        self.source = source
        self.external_id = external_id

        # Паспорт объекта
        self.psb_id = psb_id
        self.psb_link = psb_link
        self.description = description

        self.region = region
        self.district = district
        self.address = address

        self.object_type = object_type
        self.work_type = work_type
        self.stage = stage
        self.frame_type = frame_type

        self.construction_period = construction_period
        self.visit_date = visit_date

        # Пользовательские
        self.customer = customer
        self.contractor = contractor
        self.designer = designer

        self.manager = manager
        self.status = status
        self.comment = comment