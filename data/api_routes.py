BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2"

# =====================
# Employees API
# =====================
EMPLOYEES_URL = f"{BASE_URL}/pim/employees"
CREATE_EMPLOYEE = EMPLOYEES_URL
DELETE_EMPLOYEE = EMPLOYEES_URL

# =====================
# Vacancies API
# =====================
VACANCIES_URL = f"{BASE_URL}/recruitment/vacancies"

CREATE_VACANCY = VACANCIES_URL
DELETE_VACANCY = VACANCIES_URL  # f"{VACANCIES_URL}/{{id}}"

# =====================
# Candidates API
# =====================
CANDIDATES_URL = f"{BASE_URL}/recruitment/candidates"

CREATE_CANDIDATE = CANDIDATES_URL
DELETE_CANDIDATE = CANDIDATES_URL


"""BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees"

# Employees
CREATE_EMPLOYEE = f"{BASE_URL}"
DELETE_EMPLOYEE = f"{BASE_URL}"

CREATE_VACANCY = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/recruitment/vacancies"
DELETE_VACANCY = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/recruitment/vacancies"

# Recruitment 
#CREATE_CANDIDATE = f"{BASE_URL}/recruitment/candidates"
#CREATE_VACANCY = f"{BASE_URL}/recruitment/vacancies" """
