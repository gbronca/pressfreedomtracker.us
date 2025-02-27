MAYBE_BOOLEAN = [
    ('NOTHING', 'unknown'),
    ('JUST_TRUE', 'yes'),
    ('JUST_FALSE', 'no'),
]


ARREST_STATUS = [
    ('UNKNOWN', 'unknown'),
    ('DETAINED_NO_PROCESSING', 'detained and released without being processed'),
    ('DETAINED_CUSTODY', 'detained and still in custody'),
    ('ARRESTED_CUSTODY', 'arrested and still in custody'),
    ('ARRESTED_RELEASED', 'arrested and released'),
    ('CHARGED_WITHOUT_ARREST', 'charged without arrest'),
]


STATUS_OF_CHARGES = [
    ('UNKNOWN', 'unknown'),
    ('NOT_CHARGED', 'not charged'),
    ('CHARGES_PENDING', 'charges pending'),
    ('CHARGES_DROPPED', 'charges dropped'),
    ('CONVICTED', 'convicted'),
    ('ACQUITTED', 'acquitted'),
    ('PENDING_APPEAL', 'pending appeal'),
]


STATUS_OF_SEIZED_EQUIPMENT = [
    ('UNKNOWN', 'unknown'),
    ('CUSTODY', 'in custody'),
    ('RETURNED_FULL', 'returned in full'),
    ('RETURNED_PART', 'returned in part'),
]


ACTORS = [
    ('UNKNOWN', 'unknown'),
    ('LAW_ENFORCEMENT', 'law enforcement'),
    ('PRIVATE_SECURITY', 'private security'),
    ('POLITICIAN', 'politician'),
    ('PUBLIC_FIGURE', 'public figure'),
    ('PRIVATE_INDIVIDUAL', 'private individual'),
]


CITIZENSHIP_STATUS_CHOICES = [
    ('US_CITIZEN', 'U.S. citizen'),
    ('PERMANENT_RESIDENT', 'U.S. permanent resident (green card)'),
    ('NON_RESIDENT', 'U.S. non-resident'),
]


INJURY_SEVERITY = [
    ('MINOR', 'minor'),
    ('MODERATE', 'moderate'),
    ('SERIOUS', 'serious'),
    ('SEVERE', 'severe'),
    ('CRITICAL', 'critical'),
    ('FATAL', 'fatal'),
]


SUBPOENA_SUBJECT = [
    ('JOURNALIST', 'journalist'),
    ('NEWS_ORGANIZATION', 'news organization'),
    ('TECHNOLOGY', 'technology/communications company'),
    ('FINANCIAL', 'bank/financial institution'),
    ('OTHER', 'other'),
]


SUBPOENA_TYPE = [
    ('TESTIMONY_ABOUT_SOURCE', 'testimony about confidential source'),
    ('OTHER_TESTIMONY', 'other testimony'),
    ('JOURNALIST_COMMUNICATIONS', 'journalist communications or work product'),
]


SUBPOENA_STATUS = [
    ('UNKNOWN', 'unknown'),
    ('PENDING', 'pending'),
    ('DROPPED', 'dropped'),
    ('QUASHED', 'quashed'),
    ('UPHELD', 'upheld'),
    ('CARRIED_OUT', 'carried out'),
    ('IGNORED', 'ignored'),
    ('OBJECTED_TO', 'objected to'),
]

CASE_STATUS = [
    ('ONGOING', 'ongoing'),
    ('SETTLED', 'settled'),
    ('DISMISSED', 'dismissed'),
    ('UNKNOWN', 'unknown'),
    ('APPEALED', 'appealed'),
]

CASE_TYPE = [
    ('CIVIL', 'Civil'),
    ('CLASS_ACTION', 'Class Action'),
]

EQUIPMENT = [
    ('SEIZED', 'seized'),
    ('BROKEN', 'broken'),
]


DETENTION_STATUS = [
    ('HELD_IN_CONTEMPT_NO_JAIL', 'held in contempt but not jailed'),
    ('IN_JAIL', 'in jail'),
    ('RELEASED', 'released from jail'),
]


THIRD_PARTY_BUSINESS = [
    ('TELECOM', 'telecom company'),
    ('TECH_COMPANY', 'tech company'),
    ('ISP', 'internet service provider'),
    ('FINANCIAL', 'bank/financial institution'),
    ('TRAVEL', 'travel company'),
    ('OTHER', 'other'),
]


LEGAL_ORDER_TYPE = [
    ('SUBPOENA', 'subpoena'),
    ('2703', '2703(d) court order'),
    ('WARRANT', 'warrant'),
    ('NATIONAL_SECURITY_LETTER', 'national security letter'),
    ('FISA', 'FISA order'),
    ('OTHER', 'other'),
]


STATUS_OF_PRIOR_RESTRAINT = [
    ('PENDING', 'pending'),
    ('DROPPED', 'dropped'),
    ('STRUCK_DOWN', 'struck down'),
    ('UPHELD', 'upheld'),
    ('IGNORED', 'ignored'),
]
