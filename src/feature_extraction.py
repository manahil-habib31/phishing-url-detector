import re
import pandas as pd
from urllib.parse import urlparse
import tldextract

# =============================================
# INDIVIDUAL FEATURE FUNCTIONS
# =============================================

def get_url_length(url):
    """Longer URLs often used in phishing to hide real destination"""
    return len(url)

def has_at_symbol(url):
    """@ symbol tricks browser - everything before @ is ignored"""
    return 1 if '@' in url else 0

def has_ip_address(url):
    """Legitimate sites use domain names, not raw IPs"""
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    return 1 if re.search(ip_pattern, url) else 0

def get_num_dots(url):
    """Too many dots = too many subdomains = suspicious"""
    return url.count('.')

def get_num_hyphens(url):
    """Hyphens in domain name are common phishing trick e.g. paypal-secure.com"""
    domain = urlparse(url).netloc
    return domain.count('-')

def get_num_digits(url):
    """Random digits in URL = auto-generated/fake URL"""
    return sum(c.isdigit() for c in url)

def has_https(url):
    """Check if URL uses HTTPS"""
    return 1 if url.startswith('https') else 0

def get_num_subdomains(url):
    """Count subdomains - phishing URLs often have many"""
    extracted = tldextract.extract(url)
    if extracted.subdomain:
        return len(extracted.subdomain.split('.'))
    return 0

def has_suspicious_keywords(url):
    """Phishing URLs often contain urgency/trust keywords"""
    keywords = [
        'verify', 'secure', 'account', 'login',
        'update', 'confirm', 'signin', 'banking',
        'password', 'credit', 'paypal', 'ebay'
    ]
    url_lower = url.lower()
    return sum(1 for word in keywords if word in url_lower)

def is_url_shortened(url):
    """URL shorteners hide real phishing destination"""
    shorteners = [
        'bit.ly', 'tinyurl', 'goo.gl', 't.co',
        'ow.ly', 'is.gd', 'buff.ly', 'adf.ly'
    ]
    return 1 if any(s in url for s in shorteners) else 0

def get_path_depth(url):
    """Very deep paths are suspicious"""
    path = urlparse(url).path
    return path.count('/')

def get_num_special_chars(url):
    """Count special characters (%, =, &, ?, #) - phishing URLs often have many"""
    special = ['%', '=', '&', '?', '#', '~']
    return sum(url.count(c) for c in special)

def get_domain_length(url):
    """Phishing domains tend to be longer"""
    extracted = tldextract.extract(url)
    return len(extracted.domain)

def has_double_slash(url):
    """Double slash in path is suspicious redirect trick"""
    path = urlparse(url).path
    return 1 if '//' in path else 0

def get_url_entropy(url):
    """High entropy (randomness) in URL = auto-generated/phishing"""
    import math
    if not url:
        return 0
    prob = [float(url.count(c)) / len(url) for c in set(url)]
    return -sum(p * math.log2(p) for p in prob)

# =============================================
# MAIN FUNCTION - Extract all features from one URL
# =============================================

def extract_features(url):
    """
    Takes a URL string, returns a dictionary of all features.
    """
    features = {}
    
    features['url_length'] = get_url_length(url)
    features['has_at_symbol'] = has_at_symbol(url)
    features['has_ip_address'] = has_ip_address(url)
    features['num_dots'] = get_num_dots(url)
    features['num_hyphens'] = get_num_hyphens(url)
    features['num_digits'] = get_num_digits(url)
    features['has_https'] = has_https(url)
    features['num_subdomains'] = get_num_subdomains(url)
    features['suspicious_keyword_count'] = has_suspicious_keywords(url)
    features['is_shortened'] = is_url_shortened(url)
    features['path_depth'] = get_path_depth(url)
    features['num_special_chars'] = get_num_special_chars(url)
    features['domain_length'] = get_domain_length(url)
    features['has_double_slash'] = has_double_slash(url)
    features['url_entropy'] = get_url_entropy(url)
    
    return features

# =============================================
# TEST - Run this file directly to test
# =============================================

if __name__ == "__main__":
    test_urls = [
        "https://www.google.com",
        "http://paypal-secure-verify.tk/login@user/confirm",
        "http://192.168.1.1/admin/login",
        "https://bit.ly/3xK9mP",
    ]
    
    for url in test_urls:
        features = extract_features(url)
        print(f"\nURL: {url}")
        for key, value in features.items():
            print(f"  {key}: {value}")