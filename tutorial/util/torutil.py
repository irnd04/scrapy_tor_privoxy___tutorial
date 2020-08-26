from toripchanger import TorIpChanger

class TorUtil:

    tic = TorIpChanger(reuse_threshold=10, tor_password='password')

    @staticmethod
    def renew_ip():
        return TorUtil.tic.get_new_ip()

