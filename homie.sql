BEGIN TRANSACTION;
CREATE TABLE "User" (
	`Id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT NOT NULL,
	`ChatId`	TEXT NOT NULL UNIQUE,
	`Password`	TEXT NOT NULL
);
CREATE TABLE "Log" (
	`Id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`User`	INTEGER NOT NULL,
	`Action`	TEXT NOT NULL,
	`Date`	TEXT NOT NULL,
	FOREIGN KEY(`User`) REFERENCES User(Id)
);
COMMIT;
