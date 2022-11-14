from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# connection = mysql.connector.connect(host='arpudhacheck.online',
#                                          database='apqurufmu_world',
#                                          user='apqurufmu_arpudha',
#                                          password='arpudha@123')


# cursor = connection.cursor()
    
# query = "SELECT * FROM revenue"

data = [
	{
		"clientCode" : "DS",
		"clientName" : "Tanjiro Kamado",
		"beneCode" : "ACT",
		"beneName" : "Atria Conv Tech",
		"o_bene_id" : 11,
		"invoicePeriod" : "2022-05-01",
		"totalAmount" : 99999989999990.00,
		"invoiceGeneratedDate" : "2022-07-21",
		"invoiceRunningNumber" : "TR-22-000049"
	},
	{
		"clientCode" : "PK",
		"clientName" : "Praveen",
		"beneCode" : "MSI",
		"beneName" : "Micro Star International",
		"o_bene_id" : 2,
		"invoicePeriod" : "2022-09-01",
		"totalAmount" : 4192608.00,
		"invoiceGeneratedDate" : "2022-09-08",
		"invoiceRunningNumber" : "TR-22-000109"
	},
	{
		"clientCode" : "PK",
		"clientName" : "Praveen",
		"beneCode" : "LBT",
		"beneName" : "Linus Torvald",
		"o_bene_id" : 1,
		"invoicePeriod" : "2022-09-01",
		"totalAmount" : 3318472.00,
		"invoiceGeneratedDate" : "2022-09-06",
		"invoiceRunningNumber" : "TR-22-000108"
	},
	{
		"clientCode" : "ARP",
		"clientName" : "Arpudha",
		"beneCode" : "ARPBENE4",
		"beneName" : "Arpudha Bene 4",
		"o_bene_id" : 22,
		"invoicePeriod" : "2022-09-01",
		"totalAmount" : 2977880.00,
		"invoiceGeneratedDate" : "2022-09-21",
		"invoiceRunningNumber" : "TR-22-000114"
	},
	{
		"clientCode" : "ARP",
		"clientName" : "Arpudha",
		"beneCode" : "ARPCLASS1",
		"beneName" : "ARPCLASS1",
		"o_bene_id" : 25,
		"invoicePeriod" : "2022-09-01",
		"totalAmount" : 1142047.80,
		"invoiceGeneratedDate" : "2022-10-31",
		"invoiceRunningNumber" : "TR-22-000180"
	},
	{
		"clientCode" : "IT",
		"clientName" : "InsertTest",
		"beneCode" : "Test NAV456",
		"beneName" : "Test NAV",
		"o_bene_id" : 17,
		"invoicePeriod" : "2022-05-01",
		"totalAmount" : 127568.00,
		"invoiceGeneratedDate" : "2022-05-21",
		"invoiceRunningNumber" : "TR-22-000063"
	},
	{
		"clientCode" : "ARP",
		"clientName" : "Arpudha",
		"beneCode" : "ARPCLASS1",
		"beneName" : "ARPCLASS1",
		"o_bene_id" : 25,
		"invoicePeriod" : "2022-10-01",
		"totalAmount" : 118849.00,
		"invoiceGeneratedDate" : "2022-10-17",
		"invoiceRunningNumber" : "TR-22-000136"
	},
	{
		"clientCode" : "DS",
		"clientName" : "Tanjiro Kamado",
		"beneCode" : "ED",
		"beneName" : "Edward",
		"o_bene_id" : 7,
		"invoicePeriod" : "2022-09-01",
		"totalAmount" : 116128.00,
		"invoiceGeneratedDate" : "2022-09-06",
		"invoiceRunningNumber" : "TR-22-000106"
	},
	{
		"clientCode" : "ARP",
		"clientName" : "Arpudha",
		"beneCode" : "@#$%^&*()",
		"beneName" : "&^%$#$%^&",
		"o_bene_id" : 24,
		"invoicePeriod" : "2022-10-18",
		"totalAmount" : 45885.00,
		"invoiceGeneratedDate" : "2022-10-18",
		"invoiceRunningNumber" : "TR-22-000137"
	},
	{
		"clientCode" : "ARP",
		"clientName" : "Arpudha",
		"beneCode" : "ARPBENE2",
		"beneName" : "Arpudha Bene 2",
		"o_bene_id" : 21,
		"invoicePeriod" : "2022-09-01",
		"totalAmount" : 15062.00,
		"invoiceGeneratedDate" : "2022-09-21",
		"invoiceRunningNumber" : "TR-22-000112"
	},
	{
		"clientCode" : "DS",
		"clientName" : "Tanjiro Kamado",
		"beneCode" : "ED",
		"beneName" : "Edward",
		"o_bene_id" : 7,
		"invoicePeriod" : "2022-04-01",
		"totalAmount" : 14271.00,
		"invoiceGeneratedDate" : "2022-05-30",
		"invoiceRunningNumber" : "TR-22-000053"
	},
	{
		"clientCode" : "PK",
		"clientName" : "Praveen",
		"beneCode" : "fghgf",
		"beneName" : "ghfghfgh",
		"o_bene_id" : 6,
		"invoicePeriod" : "2022-04-01",
		"totalAmount" : 10294.74,
		"invoiceGeneratedDate" : "2022-05-19",
		"invoiceRunningNumber" : "TR-22-000035"
	},
	{
		"clientCode" : "DS",
		"clientName" : "Tanjiro Kamado",
		"beneCode" : "ACT",
		"beneName" : "Atria Conv Tech",
		"o_bene_id" : 11,
		"invoicePeriod" : "2022-09-01",
		"totalAmount" : 5336.00,
		"invoiceGeneratedDate" : "2022-09-01",
		"invoiceRunningNumber" : "TR-22-000110"
	},
	{
		"clientCode" : "PK",
		"clientName" : "Praveen",
		"beneCode" : "SN9941",
		"beneName" : "Sultan",
		"o_bene_id" : 10,
		"invoicePeriod" : "2022-05-01",
		"totalAmount" : 4899.00,
		"invoiceGeneratedDate" : "2022-05-11",
		"invoiceRunningNumber" : "TR-22-000047"
	},
	{
		"clientCode" : "PK",
		"clientName" : "Praveen",
		"beneCode" : "LBT",
		"beneName" : "Linus Torvald",
		"o_bene_id" : 1,
		"invoicePeriod" : "2022-02-01",
		"totalAmount" : 4166.80,
		"invoiceGeneratedDate" : "2022-02-23",
		"invoiceRunningNumber" : "TR-22-000016"
	},
	{
		"clientCode" : "PK",
		"clientName" : "Praveen",
		"beneCode" : "MSI",
		"beneName" : "Micro Star International",
		"o_bene_id" : 2,
		"invoicePeriod" : "2022-08-01",
		"totalAmount" : 2829.00,
		"invoiceGeneratedDate" : "2022-08-23",
		"invoiceRunningNumber" : "TR-22-000103"
	},
	{
		"clientCode" : "ARP",
		"clientName" : "Arpudha",
		"beneCode" : "ARPBENE3",
		"beneName" : "Arpudha Bene 3",
		"o_bene_id" : 23,
		"invoicePeriod" : "2022-09-01",
		"totalAmount" : 1849.00,
		"invoiceGeneratedDate" : "2022-09-21",
		"invoiceRunningNumber" : "TR-22-000113"
	},
	{
		"clientCode" : "INI",
		"clientName" : "NithishClient",
		"beneCode" : "DBN",
		"beneName" : "$%^&*",
		"o_bene_id" : 19,
		"invoicePeriod" : "2022-09-01",
		"totalAmount" : 1296.00,
		"invoiceGeneratedDate" : "2022-09-10",
		"invoiceRunningNumber" : "TR-22-000107"
	},
	{
		"clientCode" : "DS",
		"clientName" : "Tanjiro Kamado",
		"beneCode" : "ED",
		"beneName" : "Edward",
		"o_bene_id" : 7,
		"invoicePeriod" : "2022-10-01",
		"totalAmount" : 850.53,
		"invoiceGeneratedDate" : "2022-10-18",
		"invoiceRunningNumber" : "TR-22-000179"
	},
	{
		"clientCode" : "PK",
		"clientName" : "Praveen",
		"beneCode" : "MSI",
		"beneName" : "Micro Star International",
		"o_bene_id" : 2,
		"invoicePeriod" : "2022-04-01",
		"totalAmount" : 367.90,
		"invoiceGeneratedDate" : "2022-05-19",
		"invoiceRunningNumber" : "TR-22-000036"
	},
	{
		"clientCode" : "PK",
		"clientName" : "Praveen",
		"beneCode" : "LBT",
		"beneName" : "Linus Torvald",
		"o_bene_id" : 1,
		"invoicePeriod" : "2022-05-01",
		"totalAmount" : 274.62,
		"invoiceGeneratedDate" : "2022-04-30",
		"invoiceRunningNumber" : "TR-22-000043"
	},
	{
		"clientCode" : "PK",
		"clientName" : "Praveen",
		"beneCode" : "MSI",
		"beneName" : "Micro Star International",
		"o_bene_id" : 2,
		"invoicePeriod" : "2022-05-01",
		"totalAmount" : 184.22,
		"invoiceGeneratedDate" : "2022-05-05",
		"invoiceRunningNumber" : "TR-22-000045"
	},
	{
		"clientCode" : "ARP",
		"clientName" : "Arpudha",
		"beneCode" : "ARPBENE1",
		"beneName" : "Arpudha Bene 1",
		"o_bene_id" : 20,
		"invoicePeriod" : "2022-09-21",
		"totalAmount" : 43.00,
		"invoiceGeneratedDate" : "2022-09-21",
		"invoiceRunningNumber" : "TR-22-000115"
	},
	{
		"clientCode" : "ARP",
		"clientName" : "Arpudha",
		"beneCode" : "ARPBENE1",
		"beneName" : "Arpudha Bene 1",
		"o_bene_id" : 20,
		"invoicePeriod" : "2022-08-01",
		"totalAmount" : 43.00,
		"invoiceGeneratedDate" : "2022-09-21",
		"invoiceRunningNumber" : "TR-22-000111"
	},
	{
		"clientCode" : "PK",
		"clientName" : "Praveen",
		"beneCode" : "GOT",
		"beneName" : "Andrew",
		"o_bene_id" : 8,
		"invoicePeriod" : "2022-05-01",
		"totalAmount" : 9.00,
		"invoiceGeneratedDate" : "2022-05-08",
		"invoiceRunningNumber" : "TR-22-000046"
	},
	{
		"clientCode" : "DS",
		"clientName" : "Tanjiro Kamado",
		"beneCode" : "ED",
		"beneName" : "Edward",
		"o_bene_id" : 7,
		"invoicePeriod" : "2022-05-01",
		"totalAmount" : 1.00,
		"invoiceGeneratedDate" : "2022-05-30",
		"invoiceRunningNumber" : "TR-22-000052"
	}
]

@app.get("/")
async def root():
    # cursor.execute(query)
    # records = cursor.fetchall()

    # for x in records:
    #     print(x)
    
    
    
    return JSONResponse(content=data)

    return data
